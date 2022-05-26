# -*- coding: utf-8 -*-
"""
Created on Sat Apr 23 22:16:31 2022

@author: sinch
"""
from glob import glob
import cv2


files = glob(r'D:\AIML_Project\original_dataset\PNEUMONIA*.png')
for img in files:
    image = cv2.imread(img)
    cv2.imwrite(img[:-3]+'.jpg',image)
    
