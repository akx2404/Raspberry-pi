#blink

import time
import RPi.GPIO as GPIO #import the raaspberry pi library

GPIO.setmode(GPIO.BOARD) #to setup the broadcom chip

GPIO.setup(7, GPIO.OUT) #to tell pi that led is an output device

for i in range(3):
    GPIO.output(7, True) # or inplace of True, GPIO.HIGH can also be used
    time.sleep(1) #in seconds
    GPIO.output(7, False)
    time.sleep(1)
