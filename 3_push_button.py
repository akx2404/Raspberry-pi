import RPi.GPIO as gpio
import time
import os

btn = 19
  
gpio.setmode(gpio.BOARD)

gpio.setup(btn, gpio.IN, pull_up_down = gpio.PUD_UP)

while True:
    if (gpio.input(btn) == False):
        print("button pressed")
        time.sleep(2)

    else:
        os.system('clear')
        time.sleep(0.1)
        
