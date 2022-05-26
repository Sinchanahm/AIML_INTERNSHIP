# -*- coding: utf-8 -*-
"""
Created on Sun Apr 24 11:16:00 2022

@author: sinch
"""

import numpy as np
from PIL import Image
import cv2
import os
folder=r'D:\AIML_Project\original_dataset\PNEUMONIA'
for i in os.listdir(folder):
# Load the image in greyscale
    file=f"{folder}\\{i}"
    img = cv2.imread(file)
    im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# create a CLAHE object (Arguments are optional).
    clahe = cv2.createCLAHE(clipLimit=4.0, tileGridSize=(3,1))
    out = clahe.apply(im)
    cv2.imwrite(file,out)
    