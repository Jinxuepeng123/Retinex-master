#要不要先转换成[0,1]  2.
#取log和不取log之间有什么区别   1.
import os
import retinex
import cv2
import json
import numpy as np

data_path = 'data/our485/low'
img_list = os.listdir(data_path)
if len(img_list) == 0:
    print('Data directory is empty.')
    exit()

with open('config.json', 'r') as f:
    config = json.load(f)

for img_name in img_list:
    img = cv2.imread(os.path.join(data_path, img_name))
    HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #将V通道
    V_channel = np.zeros_like(img[:,:,0])
    V_channel=HSV_img[:,:,2]
    V_channel = np.float64(img)
    HSV_img[:,:,2]=retinex.singleScaleRetinex(V_channel,80)   #有15，80，250三个选择，先选80

    cv2.waitKey()