#!/usr/bin/python
from inputs import get_gamepad
import time
import keyboard

while 1:
	events = get_gamepad()
	for event in events:
		try:
			# debug print
			#if (event.code!='ABS_Z' and event.code!='SYN_REPORT'):
			#	print(event.ev_type, event.code, event.state)
			# end debug print
			if (event.code=='ABS_X'):
				if (event.state==0): 
					# player 1 left 
					keyboard.send('left')
				elif (event.state==255):
					# player 1 right
					keyboard.send('right')
			elif (event.code=='ABS_Y'):
				if (event.state==0): 
					# player 1 up
					keyboard.send('up')
					last_gamepad_event = 'up'
				elif (event.state==255):
					# player 1 down
					keyboard.send('down')
			elif (event.code=='BTN_TRIGGER' and event.state==1):
				# player 1 B 
				keyboard.send('enter')
			elif (event.code=='BTN_THUMB' and event.state==1):
				# player 1 A
				keyboard.send('esc')
			elif (event.code=='BTN_TOP' and event.state==1):
				# player 1 Y
				keyboard.send('right ctrl')
			elif (event.code=='BTN_TOP2' and event.state==1):
				# player 1 X
				keyboard.send('alt')
			elif (event.code=='BTN_BASE3' and event.state==1):
				# player 1 select
				keyboard.send('esc')
			elif (event.code=='BTN_BASE4' and event.state==1):
				# player 1 start
				keyboard.send('enter')
			elif (event.code=='BTN_PINKIE' and event.state==1):
				# player 1 left shoulder
				keyboard.write('c') 
		except:
			pass
