from panda3d.core import *
from direct.directnotify.DirectNotifyGlobal import *
import json

rpc_client_endpoint = ConfigVariableString(
    'rpc-client-endpoint', '',
    'Specifies the URL to the remote server where RPC events can be fired off.')

rpc_client_pool = ConfigVariableInt(
    'rpc-client-pool', 4,
    'Specifies the maximum number of concurrent connections that the RPC client'
    ' will open.')

rpc_client_retry = ConfigVariableInt(
    'rpc-client-retry', 10,
    'The number of times that the RPC client will try a retryable request'
    ' before giving up. Use 0 for unlimited, 1 for no retries, 2 for two tries'
    ' (and therefore only one retry), etc.')


class RPCCall:
    def __init__(self, client, method, params, callback, errback, tries):
        self.client = client
        self.method = method
        self.params = params
        self.callback = callback
        self.errback = errback
        self.tries = tries

        self.requestData = json.dumps({'jsonrpc': "2.0", 'id': 1,
                                       'method': method, 'params': params})
        self.stream = StringStream()

        self.channel = None

    def begin(self, channel):
        self.channel = channel

        ds = DocumentSpec(self.client.url)

        self.stream.clearData()

        self.channel.beginPostForm(ds, self.requestData)
        self.channel.downloadToStream(self.stream)

        # Add it to the channels that get .run() called each frame.
        self.client._runningChannels[self.channel] = self

    def onFailure(self):
        if self.tries == 0:
            # Unlimited tries!
            self._releaseChannel()
            self.client._enqueueCall(self)
            return
        elif self.tries <= 1:
            # We're out of tries...
            pass
        else:
            self.tries -= 1
            self._releaseChannel()
            self.client._enqueueCall(self)
            return

        # If we got here, it's an error, and we've lost.
        if self.errback:
            self.errback()
        self._releaseChannel()

    def onFinish(self):
        if not self.channel.isValid():
            self.client.notify.warning('RPC call (%s) failed to make HTTP request' % self.method)
            return self.onFailure()

        if not self.channel.isDownloadComplete():
            self.client.notify.warning('RPC call (%s) received truncated response' % self.method)
            return self.onFailure()

        # Parse out the JSON-RPC request:
        data = self.stream.getData()
        try:
            response = json.loads(data)
        except ValueError:
            self.client.notify.warning('RPC call (%s) received invalid JSON response' % self.method)
            return self.onFailure()

        error = response.get('error', None)
        if error is not None:
            self.client.notify.warning('RPC call (%s) resulted in error: %s' % (self.method, error))
            return self.onFailure()

        if 'result' not in response:
            self.client.notify.warning('RPC call (%s) did not include result' % self.method)
            return self.onFailure()

        # Success!
        if self.callback:
            self.callback(response['result'])

        self._releaseChannel()

    def _releaseChannel(self):
        assert self.channel
        channel = self.channel
        self.channel = None

        # We do this LAST, since this may result in us getting used again:
        self.client._returnChannel(channel)


class RPCClient:
    notify = directNotify.newCategory('RPCClient')

    def __init__(self, url=None):
        self.url = URLSpec(url or rpc_client_endpoint.getValue())
        self.defaultTries = rpc_client_retry.getValue()

        self.client = HTTPClient()
        self.client.setVerifySsl(0)

        self.channels = []
        self._callQueue = []
        self._availableChannels = []
        self._runningChannels = {}
        for x in xrange(rpc_client_pool.getValue()):
            channel = self.client.makeChannel(True)
            self.channels.append(channel)
            self._availableChannels.append(channel)

        self.task = taskMgr.add(self._task, 'RPCClient')

    def call(self, _method, _callback=None, _errback=None, _retry=False, **kwargs):
        if not self.url.hasServer():
            # RPC is not configured; skip.
            if _errback:
                _errback()
            return

        if _retry == True:
            tries = self.defaultTries
        elif _retry == False:
            tries = 1
        elif isinstance(_retry, (int, long)):
            tries = _retry
        else:
            assert False

        call = RPCCall(self, _method, kwargs, _callback, _errback, tries)
        self._enqueueCall(call)

    def _setHeaders(self, channel):
        channel.clearExtraHeaders()
        channel.sendExtraHeader('Connection', 'Keep-Alive')
        channel.sendExtraHeader('Accept', 'application/json')
        channel.sendExtraHeader('Content-Type', 'application/json')
        channel.sendExtraHeader('User-Agent', 'OTP RPC client')

    def _enqueueCall(self, call):
        self._callQueue.append(call)
        self._flushQueue()

    def _returnChannel(self, channel):
        # We put recent channels at the front to encourage quick reuse.
        self._availableChannels.insert(0, channel)
        self._flushQueue()

    def _flushQueue(self):
        while self._callQueue and self._availableChannels:
            call = self._callQueue.pop(0)
            channel = self._availableChannels.pop(0)
            self._setHeaders(channel)
            call.begin(channel)

    def _task(self, task):
        for channel, call in self._runningChannels.items():
            if not channel.run():
                del self._runningChannels[channel]
                call.onFinish()
        return task.cont
