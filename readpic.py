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
np.random.shuffle(training_data)


#Jeff Edited
import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout, Activation, Flatten, Conv2D, MaxPooling2D
import pickle

X = pickle.load(open("X.pickle", "rb")) # X, y 要修改
y = pickle.load(open("y.pickle", "rb"))

X = X/255.0

model = Sequential()

model.add( Conv2D(64, (3,3), input_shape = X.shape[1:]) )
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Conv2D(64), (3,3))
model.add(Activation("relu"))
model.add(MaxPooling2D(pool_size = (2,2)))

model.add(Flatten())
model.add(Dense(64))

model.add(Dense(1))
model.add(Activation("sigmoid"))

model.compile(loss = "categorical_crossentropy", optimizer = "adam", metrics = ['accuracy'])

model.fit(X, y, batch_size, epochs = 5, validation_split = 0.1)
