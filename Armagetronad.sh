#!/bin/bash
trap "exit" INT TERM ERR
#trap "sudo killall -9 gamepad_emulate.py" EXIT
# launch gamepad emulator
cd /home/pi/RetroPie/roms/ports/
sudo ./gamepad_emulate.py &
cd /home/pi/RetroPie/roms/ports/Armagetronad/
sudo ./armagetronad_main
# when done...
sudo killall -9 gamepad_emulate.py
