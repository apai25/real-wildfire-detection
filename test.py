from predict import predict
import time

while True:
    print(int(predict('images.jpeg') > 0.5))
    time.sleep(7)