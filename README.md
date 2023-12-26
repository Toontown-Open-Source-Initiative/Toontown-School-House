# Toontown-School-House
Welcome to the Toontown School House repository!

Toontown School House is a course dedicated to teaching members of the Toontown community how to develop for the game. For more information, head over to [this](https://www.reddit.com/r/Toontown/comments/doszgg/toontown_school_house_learn_to_develop_for/) Reddit post.

Feel free to join our Discord server [here!](https://discord.gg/xFGA8Xa)

This project is currently inactive, but feel free to submit pull requests and join the Discord server regardless to interact with other people who are interested in developing for Toontown.

You are free to use this project for any purpose that is not prohibited by the project's licensing. See the "License" section in this README for more details.

# Panda3D
This source code requires a customized version of Panda3D to run. Here are links to the 32 and 64 bit Windows executables. Please contact the teachers on our Discord server for instructions on the Linux Panda3D setup.

[Panda3D SDK for Windows (64-bit)](http://www.mediafire.com/file/jd64nzvtdvnyw5z/Panda3D-1.11.0-x64.exe/file)

# Using MySQL for Parties and/or Code Redemption
This source code contains both Code Redemption and Parties based off the Toontown Online source code leak (Anesidora). They both have two different styles of databases that can be used for both. These databases are the following:

Additionally, there is an RPC endpoint that can be used for code redemption to create code lots, modify code lots, and redeem codes manually. 
This can be enabled by setting `want-rpc-server #t` and using [Toontown Code Redemption NextJS Portal](https://github.com/alexbegt/TT-CR-NextJS-Portal)

## JSON 
This database format is enabled by default for both code redemption and parties. These use flat files to store the data required for each to work. This includes the following: Party Data and Invite Data for parties AND Code Lot, Code Set and Code Space for the Code Redemption.

## MySQL
In order to use the MySQL database, you will need to install the PyMYSQL library via pip. An included 'requirements.txt' is included in the root directory that can easily be used with `ppython -m pip install -r requirements.txt`.

You will need to run your own MySQL server that the client can talk to; for instance, installing MariaDB will give you a local MySQL server that you can use for the game. You will also need to create two users and two different databases and give the user you create access to change these.

By default, these are: (USER: toontown_code_redemption DB: tt_code_redemption), (USER: toontown_parties DB: tt_parties)

There is example SQL for creating these users and databases under example_user_creation.txt; Replace 'PASSWORD' with the password of your choosing.

Additionally, you will need to set/change the following configuration options inside of 'dev.prc':
### For Code Redemption
* `want-code-redemption-mysql #t`
* `tt-code-db-password PASSWORD_HERE`
#### These are optional ones that you can change (Default Values):
* `tt-code-db-host localhost`
* `tt-code-db-port 3306`
* `tt-code-db-user toontown_code_redemption`
* `tt-code-db-name tt_code_redemption`
### For Parties
* `want-parties-mysql #t`
* `tt-parties-db-password PASSWORD_HERE`
#### These are optional ones that you can change (Default Values):
* `tt-parties-db-host localhost`
* `tt-parties-db-port 3306`
* `tt-parties-db-user toontown_parties`
* `tt-parties-db-name tt_parties`

# Libuv 
This source code requires libuv.dll in the astron folder to run. Here are links to the 32 bit dll and 64 bit dll.
[Libuv.dll (32-bit)](https://cdn.discordapp.com/attachments/638485243560460309/640339222682664973/libuv.dll)
[Libuv.dll(64-bit)](https://cdn.discordapp.com/attachments/638485243560460309/640339153346887696/libuv.dll)
After downloading the file just drop it in the astron folder

# Source Code
This source code is based on a March 2019 fork of Toontown Offline v1.0.0.0. It has been stripped of all Toontown Offline exclusive features, save one. The brand new Magic Words system made for Toontown Offline has been left alone, and upgraded to the most recent build. This feature will allow users to easily navigate around Toontown without any hassle.

Credits:
* [The Toontown Offline Team](https://ttoffline.com)
* [Astron](https://github.com/Astron/Astron)
* [Panda3D](https://github.com/panda3d/panda3d) (More specifically, the modified Astron Panda3D which can be found [here](https://github.com/Astron/panda3d))
* [libpandadna](https://github.com/loblao/libpandadna)
* [libotp-movement](https://github.com/jwcotejr/libotp-movement)
* [libotp-nametags](https://github.com/loblao/libotp-nametags)
* [Toontown Rewritten](https://toontownrewritten.com)
* [Anesidora](https://github.com/satire6/Anesidora)
* Reverse-engineered Toontown Online client/server source code is property of The Walt Disney Company.

# License
See `LICENSE.md` and `resources/LICENSE.md` for licensing information.
