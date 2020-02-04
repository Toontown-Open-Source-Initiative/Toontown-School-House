@echo off
title Toontown Online - AI (District) Server - Toon Valley
cd..

rem Read the contents of PPYTHON_PATH into %PPYTHON_PATH%:
set /P PPYTHON_PATH=<PPYTHON_PATH

:main
%PPYTHON_PATH% -m toontown.ai.AIStart --base-channel 403000000 ^
               --max-channels 999999 --stateserver 4002 ^
               --astron-ip 127.0.0.1:7199 --eventlogger-ip 127.0.0.1:7199 ^
               --district-name "Toon Valley"
goto main
