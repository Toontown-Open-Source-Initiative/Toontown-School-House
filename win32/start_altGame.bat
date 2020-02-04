@echo off
title Toontown Online - Game Client - LightHappy
cd..

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

set TTOFF_LOGIN_TOKEN=dev2

%PPYTHON_PATH% -m toontown.launcher.TTOffQuickStartLauncher
pause
