# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 18:16:52 2018

@author: Jo Clark (SpaceCadetJo)
"""

#print("Hello World")

#ask the user for the feet
feet = input("How many feet are there?\n")

try:
        feet_float = float(feet)

        #convert feet to inches
        inches = feet_float*12

        #tell the user how many inches are in that many feet
        print("There's {} inches in that number of feet.".format(inches))
        
except ValueError:
        print("Hey, that wasn't a number!")
        

print("Thanks for playing!")