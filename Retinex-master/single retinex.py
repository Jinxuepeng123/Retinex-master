#要不要先转换成[0,1]  2.
#取log和不取log之间有什么区别   1.
import os
import retinex
import cv2
import json
import numpy as np

data_path = 'data/our485/low'
fine_path='data/retinex_log/'
img_list = os.listdir(data_path)
if len(img_list) == 0:
    print('Data directory is empty.')
    exit()

with open('config.json', 'r') as f:
    config = json.load(f)

img_list.sort(key= lambda x:int(x[:-4]))   #排序得好方法
for img_name in img_list:
    img = cv2.imread(os.path.join(data_path, img_name))

    HSV_img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)  #将V通道数据变为float64处理完后再将V变为unit8再再转换为图片形式，最后保存
    #创建副本以免V_channel与hsv图像公用内存
    V_channel = np.zeros_like(img[:,:,0])
    V_channel=HSV_img[:,:,2]   #V_channel赋值
    V_channel = np.float64(V_channel)    #转换成float 64，接下来对V空间进行处理，且赋值给一个中间量
    temp=retinex.SSR(V_channel,300)   #有15，80，250三个选择，先选80
    #temp = temp * 100   #数值太小了将每个像素乘以10
    #temp= np.uint8(temp)       #将temp转换到unit8,方便图像显示，接下来赋值给hsv的V

    HSV_img[:,:,2]=temp     #接下来将hsv转化到RGB
    RGB=cv2.cvtColor(HSV_img, cv2.COLOR_HSV2BGR)

    path=fine_path+img_name
    cv2.imwrite(path, RGB)  #保存的图片弄错了
    print(path,'已保存')
    #如何保存图片呢