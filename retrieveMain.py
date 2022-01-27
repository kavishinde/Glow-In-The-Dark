from firebase import firebase
import RPi.GPIO as GPIO
import time
from time import sleep     
GPIO.setwarnings(False)    
#GPIO.setmode(GPIO.BOARD)


firebase = firebase.FirebaseApplication('https://test-6969dd.firebaseio.com/', None)
while True:
    try:
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(37,GPIO.OUT)
        GPIO.setup(40,GPIO.OUT)
        
        PIN_TRIGGER = 16
        PIN_ECHO = 18
        
        GPIO.setup(PIN_TRIGGER, GPIO.OUT)
        GPIO.setup(PIN_ECHO, GPIO.IN)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        time.sleep(2)
        GPIO.output(PIN_TRIGGER, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(PIN_TRIGGER, GPIO.LOW)
        while GPIO.input(PIN_ECHO)==0:
                pulse_start_time = time.time()
        while GPIO.input(PIN_ECHO)==1:
                pulse_end_time = time.time()

        pulse_duration = pulse_end_time - pulse_start_time
        distance = round((((pulse_duration / 2) / 29)*1000000),2)
        print ("Distance:",distance,"cm")
        
        #LED 1
        LED_1 = firebase.get('/A/LED1/light', '')  
        print("LED_1 value = ",LED_1)
        if LED_1 == True and distance >= 15 :
            GPIO.output(37, GPIO.HIGH)
        else:
            GPIO.output(37, GPIO.LOW)

        #LED 10
        LED_10 = firebase.get('/A/LED10/light', '')  
        print("LED_10 value = ",LED_10)
        if LED_10 == True and distance >= 15:
            GPIO.output(40, GPIO.HIGH)
        else:
            GPIO.output(40, GPIO.LOW)

    finally:
          GPIO.cleanup()

