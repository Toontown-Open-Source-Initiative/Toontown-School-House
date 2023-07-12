# This is the PRC configuration file for settings that are
# specific to developer instances of Toontown Online.

# Window settings
window-title Toontown Online [DEV]

# Notify settings
console-output true

# Server settings
server-version tto-dev

# Developer settings
want-dev false
schellgames-dev false
exec-chat true
log-private-info true
want-qa-regression true

# Chat settings
want-whitelist false

# Audio settings
audio-library-name p3openal_audio

# Resources settings
vfs-mount resources/phase_3 /phase_3
vfs-mount resources/phase_3.5 /phase_3.5
vfs-mount resources/phase_4 /phase_4
vfs-mount resources/phase_5 /phase_5
vfs-mount resources/phase_5.5 /phase_5.5
vfs-mount resources/phase_6 /phase_6
vfs-mount resources/phase_7 /phase_7
vfs-mount resources/phase_8 /phase_8
vfs-mount resources/phase_9 /phase_9
vfs-mount resources/phase_10 /phase_10
vfs-mount resources/phase_11 /phase_11
vfs-mount resources/phase_12 /phase_12
vfs-mount resources/phase_13 /phase_13

# DC file
dc-file astron/dclass/tto.dc

# RPC
want-rpc-server #f
rpc-server-endpoint http://0.0.0.0:1337/

# Code Redemption
want-code-redemption-mysql #f
code-redemption-self-test #f
want-unique-code-generation #t

# Parties
want-parties-mysql #f
want-parties-init-db #t