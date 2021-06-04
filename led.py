import RPi.GPIO as GPIO
import time
LED_PIN_RED = 21
GPIO.setmode(GPIO.BCM)
GPIO.setup(LED_PIN_RED, GPIO.OUT)

while True:
    GPIO.output(LED_PIN_RED, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(LED_PIN_RED, GPIO.LOW)
    time.sleep(1)
GPIO.cleanup()