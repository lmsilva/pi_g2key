#!/bin/bash
./send_keypress.py &
keypress_pid=$!
./armagetronad_main
kill -9 $keypress_pid
