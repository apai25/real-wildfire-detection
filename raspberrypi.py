from cv2 import cv2
import time
import firebase, pyrebase
import geocoder

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

geo = geocoder.ip('me')
coordinates = geo.latlng
coordinate_text = f'{coordinates[0]}, {coordinates[1]}'

firebase_path = f'photo/image1.png'
local_path = 'image.png'
cam = cv2.VideoCapture(0)

while True:
    is_error, img = cam.read()
    if not is_error:
        print('Error when grabbing frame')
        break

    cv2.imwrite(local_path, img)
    storage.child(firebase_path).put(local_path)

    time.sleep(10)

    