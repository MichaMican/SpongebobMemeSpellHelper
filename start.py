#!/usr/bin/env python3

from pynput.keyboard import Key, Controller
import time

keyboard = Controller()

timeInSec = 0
while(timeInSec <= 0):
    try:
        timeInMs = input("Enter time between capslock presses in milliseconds (250ms recommended)\n")
        timeInSec = int(timeInMs)/1000.0
        break
    except:
        print("\nPlease enter a valid integer (not negative && only numbers)\n")

print("To stop the script just hit Ctrl + C")

while True: 
    keyboard.press(Key.caps_lock)
    keyboard.release(Key.caps_lock)
    time.sleep(timeInSec)
    