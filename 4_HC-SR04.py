import RPi.GPIO as GPIO
import time


GPIO.setmode(GPIO.BOARD)
trig = 16
echo = 18

while True:

    print("distance measurement in progress .... ")

    GPIO.setup(trig, GPIO.OUT)
    GPIO.setup(echo, GPIO.IN)

    GPIO.setup(trig, False)
    print("Waiting for sensor to settle ... ")
    time.sleep(2)

    GPIO.output(trig, True)
    time.sleep(0.00001)
    GPIO.output(trig, False)

    while GPIO.input(echo) ==0:
        pulse_start = time.time()

    while GPIO.input(echo) ==1:
        pulse_end = time.time()

    duration = pulse_end- pulse_start

    distance = (duration * 330)*50    #cm
    distance = round(distance, 2)

    print("Distance --- {}".format(distance))

    time.sleep(3)
    
