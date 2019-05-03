#!/usr/bin/python
from ConfigParser import SafeConfigParser
from inputs import devices
from inputs import get_gamepad
import time
import signal
import sys

def signal_handler(sig, frame):
	print
        print "Exiting!"
        sys.exit(0)
signal.signal(signal.SIGINT, signal_handler)

###### REMOVE
from inputs import get_key
###### REMOVE

print " -- Pi g2k configurator --"
if (len(devices.keyboards) > 0):
	print "Press Ctrl+C to exit when done!"
	while (1):
		############## GAMEPAD READ 
		print "Press Gamepad button..."
		GAMEPAD = None
		while (GAMEPAD == None):
			events = get_key()
			for event in events:
				if (event.ev_type == 'Key' and event.state == 1 ):
					GAMEPAD = event.code
					break
		time.sleep(1)
		print
		############## KEYBOARD READ 
		print "Map to keyboard key..."
		KEYBOARD = None
		while (KEYBOARD == None):
			events = get_key()
			for event in events:
				if (event.ev_type == 'Key' and event.state == 1 ):
					KEYBOARD = event.code
					break
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
else:
	print "No gamepads found! Exiting..."
	exit(1)
