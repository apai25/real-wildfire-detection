from picamera import PiCamera
import time
import firebase, pyrebase

config = {
    'apiKey': "AIzaSyBRPS032EMhcRCLckjdxdkMpX3QTPZo9X0",
    'authDomain': "wildfire-detection-57811.firebaseapp.com",
    'projectId': "wildfire-detection-57811",
    'storageBucket': "wildfire-detection-57811.appspot.com",
    'messagingSenderId': "63279387370",
    'appId': "1:63279387370:web:ae1517b1a068d6eff23d93",
    'measurementId': "G-TF5YM7L4G2",
    'databaseURL': None}

firebase = pyrebase.initialize_app(config)
storage = firebase.storage()

firebase_path = 'photo/image1.png'
local_path = 'image.png'

camera = PiCamera()
time.sleep(3)

while True:
    camera.capture(local_path)
    storage.child(firebase_path).put(local_path)

    time.sleep(10)

    