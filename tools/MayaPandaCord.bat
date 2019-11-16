@echo off
cls
:start

echo Enter X * 100:
set /p num1=
echo Enter Y * 100:
set /p num2=
echo Enter Z * 100:
set /p num3=

set /a sumX="num1 * -1"
set /a sumZ="num2"
set /a sumY="num3 * -1"
echo X %sumX% / 100
echo Y %sumY% / 100
echo Z %sumZ% / 100

pause
goto start
