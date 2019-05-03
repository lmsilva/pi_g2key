#!/usr/bin/python
from inputs import devices
from inputs import get_gamepad
for device in devices:
	print(device)
while 1:
	events = get_gamepad()
	for event in events:
		print(event.ev_type, event.code, event.state)
