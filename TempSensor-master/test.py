#!/usr/bin/python
# -*- coding: utf-8 -*-

import serial

TTY = "COM3"

port = serial.Serial(TTY)

for temp in port:
    temp = temp.strip()
    print "Temperature is: %s" % temp
