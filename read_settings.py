#!/usr/bin/python
from ConfigParser import SafeConfigParser
config = SafeConfigParser()
config.read('gamepad_config.ini')
print config.get('main','key1')
print config.get('main','key2')
print config.get('main','key3')
