import RPi.GPIO as GPIO
from time import sleep


GPIO.setwarnings(False)

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.OUT)
GPIO.setup(16, GPIO.OUT)


while (True):    
    
    
    GPIO.output(18, 1)
    
    sleep(5)
    
    GPIO.output(18, 0)

    sleep(1)
    
    GPIO.output(16, 1)
    
    sleep(10)
    
    GPIO.output(16, 0)
    
    sleep(1)

    break
