#!/usr/bin/python
from ConfigParser import SafeConfigParser
from inputs import devices
from inputs import get_gamepad
from inputs import get_key
import time
import keyboard

config = SafeConfigParser()
config.read('gamepad_config.ini')
while 1:
		
	events = get_gamepad()
	for event in events:
		try:
			if (event.state==0):
				keyboard.send(config.get('gamepad_mapping', event.code.upper()))
		except:
			pass
