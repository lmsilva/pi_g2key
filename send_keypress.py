#!/usr/bin/python
from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

while 1:
	keyboard.press(Key.down)
	keyboard.release(Key.down)
	time.sleep(1)
