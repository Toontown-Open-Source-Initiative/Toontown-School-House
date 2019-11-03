cd `dirname $0`
cd ..

while [ true ]
do
    /usr/bin/python2.7 -m toontown.ai.AIStart --base-channel 401000000 --max-channels 999999 --stateserver 4002 --astron-ip 127.0.0.1:7199 --eventlogger-ip 127.0.0.1:7197 --district-name "Toon Valley"
    sleep 5
done
