# -*- coding: utf-8 -*-
"""
Created on Fri Nov 28 12:53:45 2014

@author: MarcosScholl
"""
import serial  
import time  
  
locations=['COM3']    

        
for device in locations:    
    try:    
        print "Trying...",device  
        arduino = serial.Serial(device, 9600)   
        break  
    except:    
        print "Failed to connect on",device     
  
   
   
var = arduino.readline()
print var
#arduino.write('S')

txt = raw_input('Entre com alguma coisa:\n')

"""
while (var != "sair"):  
    arduino.write(txt)
    var = arduino.readline()
    print "S= "+var
    time.sleep(1)
    txt = raw_input('Entre com alguma coisa:\n')
print "Good bye!"
""        
            
#except:    
#    print "Failed to send!"   