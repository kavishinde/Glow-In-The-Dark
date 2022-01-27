from firebase import firebase
firebase = firebase.FirebaseApplication('https://test-6969dd.firebaseio.com/', None)

while(True):
    i = firebase.get('https://test-6969dd.firebaseio.com/A/', 'Occupied') 
    x=int(input("sensor data: "))
    if(x<100):
        firebase.put('https://test-6969dd.firebaseio.com/A/','Occupied',i+1)
    else:
        firebase.put('https://test-6969dd.firebaseio.com/A/','Occupied',i-1)
    print('updated')
