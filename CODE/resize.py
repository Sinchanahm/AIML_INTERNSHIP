# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 19:18:56 2022

@author: sinch
"""

from PIL import Image
import os
folder=r'D:\AIML_Project\original_dataset\PNEUMONIA'
width=256
height=256
for i in os.listdir(folder):
    file=f"{folder}\\{i}"
    im=Image.open(file)
    im=im.resize((width,height),Image.ANTIALIAS)
    im.save(file)
