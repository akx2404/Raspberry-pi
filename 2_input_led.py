import time
import RPi.GPIO as gpio

red = 11
yellow = 13
color = input("Enter the color--  ")

gpio.setmode(gpio.BOARD)

gpio.setup(red, gpio.OUT)
gpio.setup(yellow, gpio.OUT)
gpio.output(red, False)
gpio.output(yellow, False)

if color == 'red':
    gpio.output(red, True)
    gpio.output(yellow, False)

elif color == 'yellow':
    gpio.output(red, False)
    gpio.output(yellow, True)
