@echo off

taskkill /f /im astrond.exe
taskkill /f /im ppython.exe
taskkill /f /fi "windowtitle eq Toontown Online - UberDOG Server"
taskkill /f /fi "windowtitle eq Toontown Online - Astron Server"
taskkill /f /fi "windowtitle eq Toontown Online - AI (District) Server"
taskkill /f /fi "windowtitle eq Toontown Online - Game Client"

start start_astron_server.bat

ping 127.0.0.1 -n 1 > nul
start start_uberdog_server.bat

ping 127.0.0.1 -n 1 > nul
start start_ai_server.bat

ping 127.0.0.1 -n 3 > nul
start start_game.bat
