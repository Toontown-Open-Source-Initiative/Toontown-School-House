# How To Run Toontown School House On Mac:


1. Download and install brew if you haven't already: Open terminal, run this command: /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
2. Install wine: run this command : brew tap gcenx/wine\
After that run this command: brew cask install --no-quarantine wine-crossover
3. Download panda3d from the readme.\
4. Use wine to install panda3d: change directory to where you installed panda3d I will show you how to get there typically: run this command : cd ~/Downloads , if that doesn't work try cd /Users/username(change to your computer username)/Downloads, then afterwards run this command: wine Panda3D-1.11.0-x64.exe
5. After installing panda3d just run the start command files in the Darwin folder in this order: start_astron_server.command, start_uberdog_server.command and start_game.command}