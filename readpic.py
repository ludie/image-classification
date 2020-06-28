# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 16:58:56 2020

@author: louis
"""
import numpy as np
import matplotlib.pyplot as plt
import os
import cv2

DATADIR = r'C:\Users\louis\Desktop\shopee_data_competition\week2\shopee-product-detection-dataset\train\train'
CATEGORIES = [str(i) for i in range(3)]

for category in CATEGORIES:
    path = os.path.join(DATADIR, category)
    for img in os.listdir(path):

        img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
        print(img_array.shape)
        new_array = cv2.resize(img_array, (100,100))
        
        plt.imshow(img_array, cmap = 'gray')
        plt.show()
        plt.imshow(new_array, cmap = 'gray')
        plt.show()
        
        break
    break
print(img_array)
        
training_data= []

def creating_training_data():
    for category in CATEGORIES:
        path = os.path.join(DATADIR, category)
        class_num = CATEGORIES.index(category)
        for img in os.listdir(path):
            try:
                img_array = cv2.imread(os.path.join(path,img), cv2.IMREAD_GRAYSCALE)
                new_array = cv2.resize(img_array, (100,100))
                training_data.append([new_array, class_num])
            except Exception:
                pass
            
creating_training_data()
print(len(training_data))
