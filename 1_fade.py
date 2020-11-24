import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD) #usinng physical location of 'BOARD"
GPIO.setup(12, GPIO.OUT) #numbering pins by physical location
GPIO.output(12, False) #default state of the led

p= GPIO.PWM(12, 1000) #set frequency to 1KHz
p.start(0) #Start PWM output, Duty cycle = 0

try:
    while True:
        for dc in range(0,101,5): #increase duty cycle: 0~100
            p.ChangeDutyCycle(dc) #keep changing it
            time.sleep(0.05) #f=N/t ---- 1000 = 20/t ----- t= 0.05
        time.sleep(0.05) #small gap
        for dc in range(100, -1, -5): #decrease duty cycle: 100~0
            p.ChangeDutyCycle(dc)
            time.sleep(0.05)
        time.sleep(0.05) #small gap

except KeyboardInterrupt:
    p.stop() #stop duty cycle
    GPIO.output(12, True) #Turn off all leds (????)
    GPIO.cleanup()
    


