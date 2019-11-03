cd `dirname $0`
cd ..

/usr/bin/python2.7 -m toontown.uberdog.UDStart --base-channel 1000000 --max-channels 999999 --stateserver 4002 --astron-ip 127.0.0.1:7199 --eventlogger-ip 127.0.0.1:7197
