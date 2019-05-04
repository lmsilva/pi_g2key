#!/usr/bin/python
from ConfigParser import SafeConfigParser
from inputs import devices
from inputs import get_gamepad
from inputs import get_key
import time
import keyboard

while 1:
	keyboard.press(keyboard.KEY_DOWN)
	keyboard.release(keyboard.KEY_DOWN)
	time.sleep(1)
