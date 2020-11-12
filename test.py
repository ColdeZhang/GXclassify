import ORrequest
import RPi.GPIO as GPIO
import time

GPIO.setup(3, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

try:
    while True:
        if GPIO.input(3) == GPIO.LOW:
            GPIO.output(5, True)
            time.sleep(5)
            GPIO.output(5, False)
            time.sleep(5)
finally:
    GPIO.cleanup()