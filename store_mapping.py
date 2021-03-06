#!/usr/bin/python
from ConfigParser import SafeConfigParser
from inputs import devices
from inputs import get_gamepad
import time
import signal
import sys
import keyboard

def signal_handler(sig, frame):
	print
        print "Exiting!"
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

print " -- Pi g2k configurator --"
if (len(devices.keyboards) == 0):
	print "No keyboards found! Try attaching a wired keyboard..."
	exit(1)
if (len(devices.gamepads) == 0):
	print "No gamepads found! Try attaching a wired keyboard..."
	exit(1)
print "Press Ctrl+C to exit when done!"
while (1):
	############## GAMEPAD READ 
	print "Press Gamepad button..."
	GAMEPAD = None
	while (GAMEPAD == None):
		events = get_gamepad()
		for event in events:
			#print (event.ev_type, event.code, event.state)
			if (event.state == 0 and event.ev_type != "Sync"):
				GAMEPAD = event.code
				break
	############## KEYBOARD READ 
	print "Map to keyboard key..."
	KEYBOARD = None
	KEYBOARD=keyboard.read_key(suppress=False)
	print "Mapping GAMEPAD event '%s' to Keyboard key press '%s'!" % (GAMEPAD, KEYBOARD)
	time.sleep(1)
	print
	# save config
	config = SafeConfigParser()
	# try to read existing config
	config.read('gamepad_config.ini')
	try:
		# try to add ini section if it does not exist
		config.add_section('gamepad_mapping')
	except:
		pass
	# gamepad mapping
	config.set('gamepad_mapping', GAMEPAD, KEYBOARD)
	with open('gamepad_config.ini', 'w') as f:
		config.write(f)
