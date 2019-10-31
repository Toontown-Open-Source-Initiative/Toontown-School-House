@echo off
title Toontown Online - Astron Server
cd ../astron
astrond --loglevel info config/astrond.yml
pause
