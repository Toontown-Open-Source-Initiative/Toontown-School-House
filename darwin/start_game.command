cd `dirname $0`
cd ..

export TTOFF_LOGIN_TOKEN="dev"

/usr/bin/python2.7 -m toontown.launcher.TTOffQuickStartLauncher
