from cv2 import cv2
import time
from test import predict
import firebase
import pyrebase


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

image_path = 'photo/image.png'
cam = cv2.VideoCapture(0)

while True:
    is_error, img = cam.read()
    if not is_error:
        print('Error when grabbing frame')
        break

    cv2.imwrite('image.png', img)
    storage.child(image_path).put('image.png')

    time.sleep(10)

    