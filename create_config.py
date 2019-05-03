#!/usr/bin/python
from ConfigParser import SafeConfigParser
from inputs import devices
from inputs import get_gamepad
import time

###### REMOVE
from inputs import get_key
###### REMOVE

print " -- Pi g2k configurator --"
if (len(devices.keyboards) > 0):
	############## UP 
	print "Press Gamepad 'UP'!"
	GAMEPAD_UP = None
	while (GAMEPAD_UP == None):
		events = get_key()
		for event in events:
			print(event.ev_type, event.code, event.state)
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_UP = event.code
				break
	print "Mapped GAMEPAD_UP to '%s'" % GAMEPAD_UP
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_UP = None
	while (KEYBOARD_UP == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_UP = event.code
				break
	print "Mapped KEYBOARD_UP to '%s'" % KEYBOARD_UP
	time.sleep(1)
	print

	############## DOWN
	print "Press Gamepad 'DOWN'!"
	GAMEPAD_DOWN = None
	while (GAMEPAD_DOWN == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_DOWN = event.code
				break
	print "Mapped GAMEPAD_DOWN to '%s'" % GAMEPAD_DOWN
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_DOWN = None
	while (KEYBOARD_DOWN == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_DOWN = event.code
				break
	print "Mapped KEYBOARD_DOWN to '%s'" % KEYBOARD_DOWN
	time.sleep(1)
	print

	############## LEFT 
	print "Press Gamepad 'LEFT'!"
	GAMEPAD_LEFT = None
	while (GAMEPAD_LEFT == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_LEFT = event.code
				break
	print "Mapped GAMEPAD_LEFT to '%s'" % GAMEPAD_LEFT
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_LEFT = None
	while (KEYBOARD_LEFT == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_LEFT = event.code
				break
	print "Mapped KEYBOARD_LEFT to '%s'" % KEYBOARD_LEFT
	time.sleep(1)
	print

	############## RIGHT 
	print "Press Gamepad 'RIGHT'!"
	GAMEPAD_RIGHT = None
	while (GAMEPAD_RIGHT == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_RIGHT = event.code
				break
	print "Mapped GAMEPAD_RIGHT to '%s'" % GAMEPAD_RIGHT
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_RIGHT = None
	while (KEYBOARD_RIGHT == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_RIGHT = event.code
				break
	print "Mapped KEYBOARD_RIGHT to '%s'" % KEYBOARD_RIGHT
	time.sleep(1)
	print

	############## A 
	print "Press Gamepad 'A'!"
	GAMEPAD_A = None
	while (GAMEPAD_A == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_A = event.code
				break
	print "Mapped GAMEPAD_A to '%s'" % GAMEPAD_A
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_A = None
	while (KEYBOARD_A == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_A = event.code
				break
	print "Mapped KEYBOARD_A to '%s'" % KEYBOARD_A
	time.sleep(1)
	print

	############## B 
	print "Press Gamepad 'B'!"
	GAMEPAD_B = None
	while (GAMEPAD_B == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_B = event.code
				break
	print "Mapped GAMEPAD_B to '%s'" % GAMEPAD_B
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_B = None
	while (KEYBOARD_B == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_B = event.code
				break
	print "Mapped KEYBOARD_B to '%s'" % KEYBOARD_B
	time.sleep(1)
	print

	############## X 
	print "Press Gamepad 'X'!"
	GAMEPAD_X = None
	while (GAMEPAD_X == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_X = event.code
				break
	print "Mapped GAMEPAD_X to '%s'" % GAMEPAD_X
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_X = None
	while (KEYBOARD_X == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_X = event.code
				break
	print "Mapped KEYBOARD_X to '%s'" % KEYBOARD_X
	time.sleep(1)
	print

	############## Y 
	print "Press Gamepad 'Y'!"
	GAMEPAD_Y = None
	while (GAMEPAD_Y == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_Y = event.code
				break
	print "Mapped GAMEPAD_Y to '%s'" % GAMEPAD_Y
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_Y = None
	while (KEYBOARD_Y == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_Y = event.code
				break
	print "Mapped KEYBOARD_Y to '%s'" % KEYBOARD_Y
	time.sleep(1)
	print

	############## LEFT SHOULDER 
	print "Press Gamepad 'LEFT SHOULDER'!"
	GAMEPAD_LSHOULDER = None
	while (GAMEPAD_LSHOULDER == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_LSHOULDER = event.code
				break
	print "Mapped GAMEPAD_LSHOULDER to '%s'" % GAMEPAD_LSHOULDER
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_LSHOULDER = None
	while (KEYBOARD_LSHOULDER == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_LSHOULDER = event.code
				break
	print "Mapped KEYBOARD_LSHOULDER to '%s'" % KEYBOARD_LSHOULDER
	time.sleep(1)
	print

	############## RIGHT SHOULDER
	print "Press Gamepad 'RIGHT SHOULDER'!"
	GAMEPAD_RSHOULDER = None
	while (GAMEPAD_RSHOULDER == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_RSHOULDER = event.code
				break
	print "Mapped GAMEPAD_RSHOULDER to '%s'" % GAMEPAD_RSHOULDER
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_RSHOULDER = None
	while (KEYBOARD_RSHOULDER == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_RSHOULDER = event.code
				break
	print "Mapped KEYBOARD_RSHOULDER to '%s'" % KEYBOARD_RSHOULDER
	time.sleep(1)
	print

	############## LEFT TRIGGER
	print "Press Gamepad 'LEFT TRIGGER'!"
	GAMEPAD_LTRIGGER = None
	while (GAMEPAD_LTRIGGER == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_LTRIGGER = event.code
				break
	print "Mapped GAMEPAD_LTRIGGER to '%s'" % GAMEPAD_LTRIGGER
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_LTRIGGER = None
	while (KEYBOARD_LTRIGGER == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_LTRIGGER = event.code
				break
	print "Mapped KEYBOARD_LTRIGGER to '%s'" % KEYBOARD_LTRIGGER
	time.sleep(1)
	print

	############## RIGHT TRIGGER
	print "Press Gamepad 'RIGHT TRIGGER'!"
	GAMEPAD_RTRIGGER = None
	while (GAMEPAD_RTRIGGER == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_RTRIGGER = event.code
				break
	print "Mapped GAMEPAD_RTRIGGER to '%s'" % GAMEPAD_RTRIGGER
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_RTRIGGER = None
	while (KEYBOARD_RTRIGGER == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_RTRIGGER = event.code
				break
	print "Mapped KEYBOARD_RTRIGGER to '%s'" % KEYBOARD_RTRIGGER
	time.sleep(1)
	print

	############## LEFT THUMB
	print "Press Gamepad 'LEFT THUMB'!"
	GAMEPAD_LTHUMB = None
	while (GAMEPAD_LTHUMB == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_LTHUMB = event.code
				break
	print "Mapped GAMEPAD_LTHUMB to '%s'" % GAMEPAD_LTHUMB
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_LTHUMB = None
	while (KEYBOARD_LTHUMB == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_LTHUMB = event.code
				break
	print "Mapped KEYBOARD_LTHUMB to '%s'" % KEYBOARD_LTHUMB
	time.sleep(1)
	print

	############## RIGHT THUMB 
	print "Press Gamepad 'RIGHT THUMB'!"
	GAMEPAD_RTHUMB = None
	while (GAMEPAD_RTHUMB == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_RTHUMB = event.code
				break
	print "Mapped GAMEPAD_RTHUMB to '%s'" % GAMEPAD_RTHUMB
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_RTHUMB = None
	while (KEYBOARD_RTHUMB == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_RTHUMB = event.code
				break
	print "Mapped KEYBOARD_RTHUMB to '%s'" % KEYBOARD_RTHUMB
	time.sleep(1)
	print

	############## LEFT THUMB UP
	print "Press Gamepad 'LEFT THUMB UP'!"
	GAMEPAD_LTHUMB_UP = None
	while (GAMEPAD_LTHUMB_UP == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_LTHUMB_UP = event.code
				break
	print "Mapped GAMEPAD_LTHUMB_UP to '%s'" % GAMEPAD_LTHUMB_UP
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_LTHUMB_UP = None
	while (KEYBOARD_LTHUMB_UP == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_LTHUMB_UP = event.code
				break
	print "Mapped KEYBOARD_LTHUMB_UP to '%s'" % KEYBOARD_LTHUMB_UP
	time.sleep(1)
	print

	############## LEFT THUMB DOWN
	print "Press Gamepad 'LEFT THUMB DOWN'!"
	GAMEPAD_LTHUMB_DOWN = None
	while (GAMEPAD_LTHUMB_DOWN == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_LTHUMB_DOWN = event.code
				break
	print "Mapped GAMEPAD_LTHUMB_DOWN to '%s'" % GAMEPAD_LTHUMB_DOWN
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_LTHUMB_DOWN = None
	while (KEYBOARD_LTHUMB_DOWN == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_LTHUMB_DOWN = event.code
				break
	print "Mapped KEYBOARD_LTHUMB_DOWN to '%s'" % KEYBOARD_LTHUMB_DOWN
	time.sleep(1)
	print

	############## LEFT THUMB LEFT 
	print "Press Gamepad 'LEFT THUMB LEFT'!"
	GAMEPAD_LTHUMB_LEFT = None
	while (GAMEPAD_LTHUMB_LEFT == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_LTHUMB_LEFT = event.code
				break
	print "Mapped GAMEPAD_LTHUMB_LEFT to '%s'" % GAMEPAD_LTHUMB_LEFT
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_LTHUMB_LEFT = None
	while (KEYBOARD_LTHUMB_LEFT == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_LTHUMB_LEFT = event.code
				break
	print "Mapped KEYBOARD_LTHUMB_LEFT to '%s'" % KEYBOARD_LTHUMB_LEFT
	time.sleep(1)
	print

	############## LEFT THUMB RIGHT
	print "Press Gamepad 'LEFT THUMB RIGHT'!"
	GAMEPAD_LTHUMB_RIGHT = None
	while (GAMEPAD_LTHUMB_RIGHT == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_LTHUMB_RIGHT = event.code
				break
	print "Mapped GAMEPAD_LTHUMB_RIGHT to '%s'" % GAMEPAD_LTHUMB_RIGHT
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_LTHUMB_RIGHT = None
	while (KEYBOARD_LTHUMB_RIGHT == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_LTHUMB_RIGHT = event.code
				break
	print "Mapped KEYBOARD_LTHUMB_RIGHT to '%s'" % KEYBOARD_LTHUMB_RIGHT
	time.sleep(1)
	print

	############## RIGHT THUMB UP 
	print "Press Gamepad 'RIGHT THUMB UP'!"
	GAMEPAD_RTHUMB_UP = None
	while (GAMEPAD_RTHUMB_UP == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_RTHUMB_UP = event.code
				break
	print "Mapped GAMEPAD_RTHUMB_UP to '%s'" % GAMEPAD_RTHUMB_UP
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_RTHUMB_UP = None
	while (KEYBOARD_RTHUMB_UP == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_RTHUMB_UP = event.code
				break
	print "Mapped KEYBOARD_RTHUMB_UP to '%s'" % KEYBOARD_RTHUMB_UP
	time.sleep(1)
	print

	############## RIGHT THUMB DOWN 
	print "Press Gamepad 'RIGHT THUMB DOWN'!"
	GAMEPAD_RTHUMB_DOWN = None
	while (GAMEPAD_RTHUMB_DOWN == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_RTHUMB_DOWN = event.code
				break
	print "Mapped GAMEPAD_RTHUMB_DOWN to '%s'" % GAMEPAD_RTHUMB_DOWN
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_RTHUMB_DOWN = None
	while (KEYBOARD_RTHUMB_DOWN == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_RTHUMB_DOWN = event.code
				break
	print "Mapped KEYBOARD_RTHUMB_DOWN to '%s'" % KEYBOARD_RTHUMB_DOWN
	time.sleep(1)
	print

	############## RIGHT THUMB LEFT 
	print "Press Gamepad 'RIGHT THUMB LEFT'!"
	GAMEPAD_RTHUMB_LEFT = None
	while (GAMEPAD_RTHUMB_LEFT == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_RTHUMB_LEFT = event.code
				break
	print "Mapped GAMEPAD_RTHUMB_LEFT to '%s'" % GAMEPAD_RTHUMB_LEFT
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_RTHUMB_LEFT = None
	while (KEYBOARD_RTHUMB_LEFT == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_RTHUMB_LEFT = event.code
				break
	print "Mapped KEYBOARD_RTHUMB_LEFT to '%s'" % KEYBOARD_RTHUMB_LEFT
	time.sleep(1)
	print

	############## RIGHT THUMB RIGHT 
	print "Press Gamepad 'RIGHT THUMB RIGHT'!"
	GAMEPAD_RTHUMB_RIGHT = None
	while (GAMEPAD_RTHUMB_RIGHT == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_RTHUMB_RIGHT = event.code
				break
	print "Mapped GAMEPAD_RTHUMB_RIGHT to '%s'" % GAMEPAD_RTHUMB_RIGHT
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_RTHUMB_RIGHT = None
	while (KEYBOARD_RTHUMB_RIGHT == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_UP = event.code
				break
	print "Mapped KEYBOARD_RTHUMB_RIGHT to '%s'" % KEYBOARD_RTHUMB_RIGHT
	time.sleep(1)
	print

	############## START 
	print "Press Gamepad 'START'!"
	GAMEPAD_START = None
	while (GAMEPAD_START == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_START = event.code
				break
	print "Mapped GAMEPAD_START to '%s'" % GAMEPAD_START
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_START = None
	while (KEYBOARD_START == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_STARTP = event.code
				break
	print "Mapped KEYBOARD_START to '%s'" % KEYBOARD_START
	time.sleep(1)
	print

	############## SELECT 
	print "Press Gamepad 'SELECT'!"
	GAMEPAD_SELECT = None
	while (GAMEPAD_SELECT == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				GAMEPAD_SELECT = event.code
				break
	print "Mapped GAMEPAD_SELECT to '%s'" % GAMEPAD_SELECT
	time.sleep(1)
	print
	print "Map to keyboard key..."
	KEYBOARD_SELECT = None
	while (KEYBOARD_SELECT == None):
		events = get_key()
		for event in events:
			if (event.ev_type == 'Key' and event.state == 1 ):
				KEYBOARD_SELECT = event.code
				break
	print "Mapped KEYBOARD_SELECT to '%s'" % KEYBOARD_SELECT
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
	# gamepad mappings
	config.set('gamepad_mapping', 'GAMEPAD_UP', GAMEPAD_UP)
	config.set('gamepad_mapping', 'GAMEPAD_DOWN', GAMEPAD_DOWN)
	config.set('gamepad_mapping', 'GAMEPAD_LEFT', GAMEPAD_LEFT)
	config.set('gamepad_mapping', 'GAMEPAD_RIGHT', GAMEPAD_RIGHT)
	config.set('gamepad_mapping', 'GAMEPAD_A', GAMEPAD_A)
	config.set('gamepad_mapping', 'GAMEPAD_B', GAMEPAD_B)
	config.set('gamepad_mapping', 'GAMEPAD_X', GAMEPAD_X)
	config.set('gamepad_mapping', 'GAMEPAD_Y', GAMEPAD_Y)
	config.set('gamepad_mapping', 'GAMEPAD_LSHOULDER', GAMEPAD_LSHOULDER)
	config.set('gamepad_mapping', 'GAMEPAD_RSHOULDER', GAMEPAD_RSHOULDER)
	config.set('gamepad_mapping', 'GAMEPAD_LTRIGGER', GAMEPAD_LTRIGGER)
	config.set('gamepad_mapping', 'GAMEPAD_RTRIGGER', GAMEPAD_RTRIGGER)
	config.set('gamepad_mapping', 'GAMEPAD_LTHUMB', GAMEPAD_LTHUMB)
	config.set('gamepad_mapping', 'GAMEPAD_RTHUMB', GAMEPAD_RTHUMB)
	config.set('gamepad_mapping', 'GAMEPAD_LTHUMB_UP', GAMEPAD_LTHUMB_UP)
	config.set('gamepad_mapping', 'GAMEPAD_LTHUMB_DOWN', GAMEPAD_LTHUMB_DOWN)
	config.set('gamepad_mapping', 'GAMEPAD_LTHUMB_LEFT', GAMEPAD_LTHUMB_LEFT)
	config.set('gamepad_mapping', 'GAMEPAD_LTHUMB_RIGHT', GAMEPAD_LTHUMB_RIGHT)
	config.set('gamepad_mapping', 'GAMEPAD_RTHUMB_UP', GAMEPAD_RTHUMB_UP)
	config.set('gamepad_mapping', 'GAMEPAD_RTHUMB_DOWN', GAMEPAD_RTHUMB_DOWN)
	config.set('gamepad_mapping', 'GAMEPAD_RTHUMB_LEFT', GAMEPAD_RTHUMB_LEFT)
	config.set('gamepad_mapping', 'GAMEPAD_RTHUMB_RIGHT', GAMEPAD_RTHUMB_RIGHT)
	config.set('gamepad_mapping', 'GAMEPAD_START', GAMEPAD_START)
	config.set('gamepad_mapping', 'GAMEPAD_SELECT', GAMEPAD_SELECT)
	# keyboard mappings
	config.set('gamepad_mapping', 'KEYBOARD_UP', KEYBOARD_UP)
	config.set('gamepad_mapping', 'KEYBOARD_DOWN', KEYBOARD_DOWN)
	config.set('gamepad_mapping', 'KEYBOARD_LEFT', KEYBOARD_LEFT)
	config.set('gamepad_mapping', 'KEYBOARD_RIGHT', KEYBOARD_RIGHT)
	config.set('gamepad_mapping', 'KEYBOARD_A', KEYBOARD_A)
	config.set('gamepad_mapping', 'KEYBOARD_B', KEYBOARD_B)
	config.set('gamepad_mapping', 'KEYBOARD_X', KEYBOARD_X)
	config.set('gamepad_mapping', 'KEYBOARD_Y', KEYBOARD_Y)
	config.set('gamepad_mapping', 'KEYBOARD_LSHOULDER', KEYBOARD_LSHOULDER)
	config.set('gamepad_mapping', 'KEYBOARD_RSHOULDER', KEYBOARD_RSHOULDER)
	config.set('gamepad_mapping', 'KEYBOARD_LTRIGGER', KEYBOARD_LTRIGGER)
	config.set('gamepad_mapping', 'KEYBOARD_RTRIGGER', KEYBOARD_RTRIGGER)
	config.set('gamepad_mapping', 'KEYBOARD_LTHUMB', KEYBOARD_LTHUMB)
	config.set('gamepad_mapping', 'KEYBOARD_RTHUMB', KEYBOARD_RTHUMB)
	config.set('gamepad_mapping', 'KEYBOARD_LTHUMB_UP', KEYBOARD_LTHUMB_UP)
	config.set('gamepad_mapping', 'KEYBOARD_LTHUMB_DOWN', KEYBOARD_LTHUMB_DOWN)
	config.set('gamepad_mapping', 'KEYBOARD_LTHUMB_LEFT', KEYBOARD_LTHUMB_LEFT)
	config.set('gamepad_mapping', 'KEYBOARD_LTHUMB_RIGHT', KEYBOARD_LTHUMB_RIGHT)
	config.set('gamepad_mapping', 'KEYBOARD_RTHUMB_UP', KEYBOARD_RTHUMB_UP)
	config.set('gamepad_mapping', 'KEYBOARD_RTHUMB_DOWN', KEYBOARD_RTHUMB_DOWN)
	config.set('gamepad_mapping', 'KEYBOARD_RTHUMB_LEFT', KEYBOARD_RTHUMB_LEFT)
	config.set('gamepad_mapping', 'KEYBOARD_RTHUMB_RIGHT', KEYBOARD_RTHUMB_RIGHT)
	config.set('gamepad_mapping', 'KEYBOARD_START', KEYBOARD_START)
	config.set('gamepad_mapping', 'KEYBOARD_SELECT', KEYBOARD_SELECT)

	with open('gamepad_config.ini', 'w') as f:
		config.write(f)
else:
	print "No gamepads found! Exiting..."
	exit(1)
