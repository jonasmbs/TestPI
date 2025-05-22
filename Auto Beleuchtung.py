
import time
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(18, GPIO.OUT) 
GPIO.setup(20, GPIO.OUT) 
GPIO.setup(13, GPIO.OUT) 
GPIO.setup(19, GPIO.IN) #Beleuchtung
GPIO.setup(26, GPIO.IN) #links
GPIO.setup(21, GPIO.IN) #Rechts


while True:


    if GPIO.input(19)==True: #Beleuchtung
        GPIO.output(18, True)
    else:
        GPIO.output(18, False)

    if GPIO.input(26)==True: #Links
        GPIO.output(13, True)
        time.sleep(0.5)
        GPIO.output(13, False)
        time.sleep(0.5)
    else:
        GPIO.output(13, False)

    if GPIO.input(21)==True: #Rechts
        GPIO.output(20, True)
        time.sleep(0.5)
        GPIO.output(20, False)
        time.sleep(0.5)
    else:
        GPIO.output(20, False)
