from firebase import firebase  
firebase = firebase.FirebaseApplication('https://test-6969dd.firebaseio.com/', None)  
data =  { 'Seat No': 'Zahaan',  
          'RollNo': 2,  
          'Percentage': 76.02  
          }  
result = firebase.post('/python-sample-ed7f7/Students/',data)  
print(result)  
