#!/usr/bin/env python3

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

while True: 
    keyboard.press(Key.caps_lock)
    keyboard.release(Key.caps_lock)
    time.sleep(0.1)
    