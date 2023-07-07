from panda3d.core import *
from direct.directnotify.DirectNotifyGlobal import *
from direct.fsm.FSM import *

from otp.otpbase import PythonUtil
import urlparse
import binascii
import json
import asyncore
import asynchat
import socket
import httplib
import time

rpc_server_endpoint = ConfigVariableString(
    'rpc-server-endpoint', '',
    'Specifies the URL that the RPC-server will listen on.')

rpc_server_listen = ConfigVariableInt(
    'rpc-server-listen', 5,
    'Specifies the depth of the listening socket\'s listen queue.')

rpc_server_polltime = ConfigVariableInt(
    'rpc-server-polltime', 2,
    'Specifies the number of milliseconds, per polling iteration, to wait for'
    ' incoming requests.')

rpc_server_polliters = ConfigVariableInt(
    'rpc-server-polliters', 5,
    'Specifies the number of polling iterations to perform each frame.')

rpc_server_keepalive = ConfigVariableInt(
    'rpc-server-keepalive', 5,
    'How many seconds the server will leave a Keep-Alive connection open.')


class RPCServer(asyncore.dispatcher):
    notify = directNotify.newCategory('RPCServer')

    def __init__(self, handler, url=None):
        asyncore.dispatcher.__init__(self)

        self.handler = handler
        url = urlparse.urlparse(url or rpc_server_endpoint.getValue())

        if url.scheme and url.scheme != 'http':
            self.notify.error('Scheme must be HTTP, not %s!' % url.scheme)

        # Parse out hostname/port:
        hostname = url.hostname
        port = url.port or 80

        if hostname is None:
            # We're not interested in running an RPC server on this process...
            return

        # Parse out authentication info:
        username = url.username
        password = url.password

        auth = username
        if password is not None:
            auth += ':' + password

        if auth is not None:
            self.auth = binascii.b2a_base64(auth).strip()
        else:
            self.auth = None

        # Parse out required path:
        self.path = url.path or '/'

        # Next, initialize the socket:
        self.create_socket(socket.AF_INET, socket.SOCK_STREAM)
        self.set_reuse_addr()
        self.bind((hostname, port))
        self.listen(5)

        # Now launch the event-handling task:
        taskMgr.add(self.task, 'RPCServer')

    def task(self, task):
        timeout = rpc_server_polltime.getValue() * 0.001
        count = rpc_server_polliters.getValue()
        asyncore.loop(timeout=timeout, count=count)
        return task.cont

    def handle_accept(self):
        pair = self.accept()
        if pair is None:
            return
        sock, addr = pair
        RPCConnection(sock, self)


class RPCConnection(asynchat.async_chat, FSM):
    def __init__(self, sock, server):
        asynchat.async_chat.__init__(self, sock=sock)
        FSM.__init__(self, 'RPCConnection')

        self.server = server

        # Defaults, in case stuff shows up before we switch states:
        self.data = ''
        self.found_terminator = lambda: None

        self.path = ''
        self.headers = {}
        self.id = None

        self.keepAlive = False
        self.timeout = None

        self.demand('ReadHeaders')

    def collect_incoming_data(self, data):
        self.data += data

    def handle_close(self):
        self.demand('Off')
        asynchat.async_chat.handle_close(self)

    def enterReadHeaders(self):
        self.data = ''
        self.set_terminator('\r\n\r\n')
        self.found_terminator = self.__got_headers

    def __got_headers(self):
        self.set_terminator(None)

        # We assume no keep-alive unless it's included specifically in the
        # request:
        self.keepAlive = False

        # Parse headers:
        for i, line in enumerate(self.data.split('\n')):
            line = line.rstrip('\r')

            if i == 0:
                # This is the HTTP request.
                request = line.split(' ')
                if len(request) != 3:
                    return self.demand('HTTPError', 400)

                method, path, version = tuple(request)

                if method != 'POST':
                    return self.demand('HTTPError', 501)

                if version not in ('HTTP/1.0', 'HTTP/1.1'):
                    return self.demand('HTTPError', 505)

                self.path = path
            else:
                # This is an HTTP header:
                header = line.split(': ')
                if len(header) != 2:
                    return self.demand('HTTPError', 400)

                key, value = tuple(header)
                self.headers[key.lower()] = value

        # Let's see if this is a keep-alive connection or not:
        if (self.headers.get('connection', '').lower() == 'keep-alive'):
            self.keepAlive = True

        # Headers parsed; on to fulfillment!
        self.demand('ReceiveData')

    def enterReceiveData(self):
        # Okay, so, we need to have a content-length, or we can't receive POST
        # data.
        length = self.headers.get('content-length', '')
        if not length or not length.isdigit():
            return self.demand('HTTPError', 400)

        length = int(length)

        self.data = ''
        self.set_terminator(length)
        self.found_terminator = self.__got_post
        self.setTimeout(None)

    def __got_post(self):
        self.set_terminator(None)

        # Since we now have the *full* request, we can now decide if we want to
        # throw out the request based on headers and junk.
        if self.server.auth is not None:
            if self.headers.get('authorization') != 'Basic ' + self.server.auth:
                return self.demand('HTTPError', 401)

        if self.server.path != self.path:
            return self.demand('HTTPError', 404)

        self.id = None

        try:
            request = json.loads(self.data)
        except ValueError:
            return self.demand('JSONError', -32700, 'Parse error')

        if 'method' not in request or 'params' not in request:
            return self.demand('JSONError', -32600, 'Invalid Request')

        self.id = request.get('id')

        if not isinstance(request['method'], basestring) or \
           not isinstance(request['params'], (tuple, list, dict)):
            return self.demand('JSONError', -32600, 'Invalid Request')

        method = getattr(self.server.handler, 'rpc_' + str(request['method']), None)
        params = request['params']
        if not method:
            return self.demand('JSONError', -32601, 'Method not found')

        request = RPCRequest(self)
        try:
            if isinstance(params, dict):
                result = method(request, **params)
            else:
                result = method(request, *params)
        except Exception:
            self.demand('JSONError', -1, PythonUtil.describeException())
        else:
            if result != request:  # Returning "request" signifies deference.
                if request.active:
                    request.result(result)

    def enterOff(self):
        self.setTimeout(None)
        self.close_when_done()

    def setTimeout(self, timeout):
        # Sets a timeout, in seconds, that we will wait for before closing the
        # connection.

        if self.timeout is not None:
            self.timeout.remove()

        if timeout is not None:
            self.timeout = taskMgr.doMethodLater(timeout, self.demand,
                                                 'RPCConnection-timeout-%d' % id(self),
                                                 extraArgs=['Off'])

    def sendResponse(self, body, contentType=None, code=200):
        # First, look up a description for the code:
        description = httplib.responses.get(code, 'Code %d' % code)

        # Prepare response:
        response = 'HTTP/1.1 %d %s\r\n' % (code, description)

        # Add standard headers:
        response += 'Date: %s\r\n' % time.strftime('%a, %d %b %Y %H:%M:%S GMT', time.gmtime())
        response += 'Server: OTP-RPCServer/0.3\r\n'

        # Add content headers:
        response += 'Content-Length: %d\r\n' % len(body)
        if contentType:
            response += 'Content-Type: %s\r\n' % contentType

        # Add authentication headers:
        if self.server.auth is not None:
            # We take security seriously:
            response += 'WWW-Authenticate: Basic realm="OTP RPC server"\r\n'

        # Add keep-alive headers:
        if self.keepAlive:
            response += 'Keep-Alive: timeout=%d\r\n' % rpc_server_keepalive.getValue()
            response += 'Connection: Keep-Alive\r\n'
        else:
            response += 'Connection: close\r\n'

        # Finally, embed the body:
        response += '\r\n' + body

        # Now send it off:
        self.push(response)

        if self.keepAlive:
            self.setTimeout(rpc_server_keepalive.getValue())
            self.demand('ReadHeaders')
        else:
            self.demand('Off')

    def sendJSON(self, data):
        body = json.dumps(data) + '\n'

        self.sendResponse(body, 'application/json', 200)

    # Error handlers:
    def enterHTTPError(self, code):
        self.server.notify.warning('Received bad HTTP request: Error code %d' % code)

        # First, look up a description for the code:
        description = httplib.responses.get(code, 'Code %d' % code)

        # Now we send our response:
        self.sendResponse('%d %s\n' % (code, description),
                          'text/plain', code)

    def enterJSONError(self, code, message):
        self.server.notify.warning('Received bad JSON request: Error code %d' % code)

        response = {'jsonrpc': '2.0',
                    'error': {'code': code,
                              'message': message},
                    'id': self.id}

        self.sendJSON(response)


class RPCRequest:
    def __init__(self, connection):
        self.connection = connection

        self.active = True

    def result(self, result):
        assert self.active
        self.active = False

        self.connection.sendJSON({'jsonrpc': '2.0',
                                  'result': result,
                                  'id': self.connection.id})

    def error(self, code, message):
        assert self.active
        self.active = False

        self.connection.demand('JSONError', code, message)
