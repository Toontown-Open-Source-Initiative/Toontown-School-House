#!/bin/sh
cd ..

echo "Toontown Online Developer Mini-Server Launcher"
echo
echo "NOTE: Make sure that \"mini-server\" is enabled in your settings.json!"
echo

read -p "Username (default: dev): " ttoffLoginToken
read -p "Game Server (default: 127.0.0.1): " ttoffGameServer

export TTOFF_LOGIN_TOKEN=${ttoffLoginToken}
export TTOFF_GAME_SERVER=${ttoffGameServer}

/usr/bin/python2 -m toontown.launcher.TTOffQuickStartLauncher
