import time
import Adafruit_DHT
import RPi.GPIO as GPIO

DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 8 
FAN_PIN = 18  # Change this to the GPIO pin your fan is connected to

GPIO.setmode(GPIO.BCM)
GPIO.setup(FAN_PIN, GPIO.OUT)

temp = 0
fan_on = False

def fan(fan_on):
    if fan_on:
        GPIO.output(FAN_PIN, GPIO.HIGH)  # Turn on the fan
    else:
        GPIO.output(FAN_PIN, GPIO.LOW)  # Turn off the fan

def checktemp():
    global temp
    try:
        humidity, temp = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        print(humidity,temp)
    except KeyboardInterrupt:
        print("error in reading")

while True:
    checktemp()
    if temp >= 21:
        fan_on = True
    else:
        fan_on = False
    fan(fan_on)
    time.sleep(1)
