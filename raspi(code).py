import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import Adafruit_DHT
import time


cred = credentials.Certificate("/Users/pradhammummaleti/Desktop/jupyter/credentials.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://raspberrypi-7ef29-default-rtdb.firebaseio.com/'
})

ref = db.reference('/') 

sensor = Adafruit_DHT.DHT11
pin = 21

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*C  Humidity={1:0.1f}%'.format(temperature, humidity))
        data = {"Temperature": temperature, "Humidity": humidity}
        new_data_ref = ref.push(data)  
        print("Sent to Firebase")
    else:
        print('Failed to get reading. Try again!')
    time.sleep(1)


#firebase_admin.delete_app(firebase_admin.get_app())
