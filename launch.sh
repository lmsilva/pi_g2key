#!/bin/bash
./send_keypress.py &
keypress_pid=$!
armagetronad
kill -9 $keypress_pid
