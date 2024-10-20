import os
import cv2

files = os.listdir('images')

for i, img in enumerate(files):
	x = cv2.imread(os.path.join(os.getcwd(), 'images', img))
	print(i, img, x.shape)