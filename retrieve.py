from firebase import firebase  
firebase = firebase.FirebaseApplication('https://test-6969dd.firebaseio.com/', None)
while True:
    #LED 1
    LED_1 = firebase.get('/A/LED1/light', '')  
    print("LED_1 value = ",LED_1)
    if LED_1 == True:
        print("True") # GPIO.output(8, GPIO.HIGH)
    else:
        print("False") # GPIO.output(8, GPIO.LOW)

    #LED 10
    LED_10 = firebase.get('/A/LED10/light', '')  
    print("LED_10 value = ",LED_10)
    if LED_10 == True:
        print("True") # GPIO.output(8, GPIO.HIGH)
    else:
        print("False") # GPIO.output(8, GPIO.LOW)



