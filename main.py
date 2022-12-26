import RPi.GPIO as gpio
import time 

carLedRed = 2
carLedYellow = 3
carLedGreen = 4
humanLedRed = 20
humanLedGreen = 21

gpio.setmode(gpio.BCM)
gpio.setup(carLedRed, gpio.OUT)
gpio.setup(carLedYellow, gpio.OUT)
gpio.setup(carLedGreen, gpio.OUT)
gpio.setup(humanLedRed, gpio.OUT)
gpio.setup(humanLedGreen, gpio.OUT)

try:
    while 1:
        gpio.output(carLedRed, gpio.LOW)
        gpio.output(carLedYellow, gpio.LOW)
        gpio.output(carLedGreen, gpio.HIGH)
        gpio.output(humanLedRed, gpio.HIGH)
        gpio.output(humanLedGreen, gpio.LOW)
        time.sleep(3)
        gpio.output(carLedRed, gpio.LOW)
        gpio.output(carLedYellow, gpio.HIGH)
        gpio.output(carLedGreen, gpio.LOW)
        gpio.output(humanLedRed, gpio.HIGH)
        gpio.output(humanLedGreen, gpio.LOW)
        time.sleep(1)
        gpio.output(carLedRed, gpio.HIGH)
        gpio.output(carLedYellow, gpio.LOW)
        gpio.output(carLedGreen, gpio.LOW)
        gpio.output(humanLedRed, gpio.LOW)
        gpio.output(humanLedGreen, gpio.HIGH)
        time.sleep(3)
                
except KeyboardInterrupt:
    pass

gpio.cleanup()