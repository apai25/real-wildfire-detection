from tensorflow.keras.models import load_model
import numpy as np 
from tensorflow.keras.preprocessing.image import load_img, img_to_array
import firebase, pyrebase
import time

def predict(image_path):
    cnn = load_model('model')
    image = load_img(image_path, target_size=(128, 128))
    image = img_to_array(image)
    image = np.expand_dims(image, axis=0)
    prediction = cnn.predict(image)[0][0]
    return prediction

locations = {
    '1': '34, 34'
}

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

count = 1
while True:
    firebase_path = f'photo/image{count}.png'
    local_path = f'photo/image{count}.png'
    storage.child(firebase_path).download(local_path)

    prediction = predict(local_path)
    if prediction == 1:
        print(f'Wildfire at {locations[str(count)]}')
    elif prediction == 0:
        print(f'Not a wildfire at {locations[str(count)]}')
    
    time.sleep(10)
