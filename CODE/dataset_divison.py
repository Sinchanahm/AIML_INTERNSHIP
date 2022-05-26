# -*- coding: utf-8 -*-
"""
Created on Sun May  1 20:35:53 2022

@author: sinch
"""

import splitfolders

input_folder = 'D:\AIML_Project\original_dataset

#split with a ratio
#train, val, test
splitfolders.ratio(input_folder,output = "CLASSIFY_DATA",seed = 42,ratio=(.8, .0, .2),group_prefix=None)