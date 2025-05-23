
import time
import RPi.GPIO as GPIO
import dht11
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) #Beleuchtung Ausgang
GPIO.setup(20, GPIO.OUT) #Blinker rechts Ausgang
GPIO.setup(13, GPIO.OUT) #Blinker links Ausgang
GPIO.setup(22, GPIO.OUT) #Sensor LED Ausgang
GPIO.setup(19, GPIO.IN) #Beleuchtung Eingang
GPIO.setup(26, GPIO.IN) #Blinker links Eingang
GPIO.setup(21, GPIO.IN) #Blinker rechts Eingang
GPIO.setup(6, GPIO.IN) #Sensor Eingang


while True:

    if GPIO.input(19)==True: #Beleuchtung
        GPIO.output(18, True)
    else:
        GPIO.output(18, False)

    if GPIO.input(26)==True: #Blinker links
        GPIO.output(13, True)
        time.sleep(0.5)
        GPIO.output(13, False)
        time.sleep(0.5)
    else:
        GPIO.output(13, False)

    if GPIO.input(21)==True: #Blinker rechts
        GPIO.output(20, True)
        time.sleep(0.5)
        GPIO.output(20, False)
        time.sleep(0.5)
    else:
        GPIO.output(20, False)


    sensor = dht11.DHT11(pin=6) #Sensor
    indoor = sensor.read()
    if indoor.is_valid():
        print("Temperatur: "  + str(indoor.temperature))
        
        if indoor.temperature >= 25:
            GPIO.output(22, True)
        else:
            GPIO.output(22, False)