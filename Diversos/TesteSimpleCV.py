# -*- coding: utf-8 -*-
"""
Created on Sat Feb 01 02:39:12 2014

@author: MarcosScholl
"""

from SimpleCV import Display, Camera
 
display = SimpleCV.Display()
cam = SimpleCV.Camera()
 
while display.isNotDone():
    img = cam.getImage().flipHorizontal()
    lines = img.findLines()
    if (lines):
        lines.draw((255,0,0))
    img.show()