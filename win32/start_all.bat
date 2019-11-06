@echo off

start start_astron_server.bat

ping 192.0.2.2 -n 1 -w 300 > nul
start start_uberdog_server.bat

ping 192.0.2.2 -n 1 -w 300 > nul
start start_nuttyriver.bat

ping 192.0.2.2 -n 1 -w 300 > nul
start start_nuttysummit.bat

ping 192.0.2.2 -n 1 -w 300 > nul
start start_toonvalley.bat

ping 192.0.2.2 -n 1 -w 1500 > nul
start start_game.bat
