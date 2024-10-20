# import cv2

# cap = cv2.VideoCapture(0)

# while True:
#     _, frame = cap.read()
#     cv2.imshow("fr", frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         cap.release()
#         break



# # rtsp://192.168.1.4:8080/h264_ulaw.sdp



# from tensorflow.python.client import device_lib
# def get_available_devices():
#     local_device_protos = device_lib.list_local_devices()
#     return [x.name for x in local_device_protos if x.device_type == 'GPU' or x.device_type == 'CPU']

# print(get_available_devices())



import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import cv2
import tensorflow as tf
import numpy as np

from time import sleep, time


from tensorflow.keras.models import load_model



print('[info] : with CPU')
image = cv2.imread('./yolov5/ss1.png')

t1 = time()
with tf.device('/cpu:0'):
    
    model = load_model('./classifier/resnet50.h5')

    image = cv2.resize(image, (224, 224))
    image = np.expand_dims(image, axis=0)
    image = tf.convert_to_tensor(image)
    print(model.predict(image))

t2 = time()

print(t2 - t1)


sleep(10)


image = cv2.imread('./yolov5/ss1.png')

print('[info] : with GPU')
t1 = time()
with tf.device('/gpu:0'):
    
    model = load_model('./classifier/resnet50.h5')

    image = cv2.resize(image, (224, 224))
    image = np.expand_dims(image, axis=0)
    image = tf.convert_to_tensor(image)
    print(model.predict(image))

t2 = time()

print(t2 - t1)




