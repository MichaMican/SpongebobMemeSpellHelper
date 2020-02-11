#!/usr/bin/env python3

from pynput.keyboard import Key, Controller
import time
import random

random.seed(int(round(time.time() * 1000)))
keyboard = Controller()

timeToSleep = 0
randomMode = False
while(timeToSleep <= 0 or randomMode):
    try:
        userInput = input("Enter time between capslock presses in milliseconds (250ms recommended). Enter 'r' for a random time between key presses\n")
        if userInput == 'r':
            randomMode = True
            break
        timeToSleep = int(userInput)/1000.0
        break
    except:
        print("\nPlease enter a valid integer (not negative && only numbers) or 'r'\n")

print("To stop the script just hit Ctrl + C")

while True: 
    keyboard.press(Key.caps_lock)
    keyboard.release(Key.caps_lock)
    if randomMode:
        timeToSleep = random.randrange(1, 250, 1)/1000.0
    
    time.sleep(timeToSleep)
    
    