# -*- coding: utf-8 -*-
"""
Created on Wed Mar 19 14:51:07 2014

@author: MarcosScholl
"""

# / Usr / bin / python
# - * - Coding: utf-8 - * -
import sys
from PyQt4 import QtGui, QtCore
from TesteSignal_Slot import *


class Example(QtGui.QWidget):
    
    def __init__(self):
        super(Example, self).__init__()
        
        self.initUI()
        
        
        
    def initUI(self):
        
        lcd = QtGui.QLCDNumber(self)
        sld = QtGui.QSlider(QtCore.Qt.Horizontal, self)
        sld.setMinimum = -360   
        sld.setMaximum = 360
        vbox = QtGui.QVBoxLayout()
        vbox.addWidget(lcd)
        vbox.addWidget(sld)

        self.setLayout(vbox)
        sld.valueChanged.connect(lcd.display)
        self.timer = QtCore.QTimer()

        #self.connect(self.timer, QtCore.SIGNAL("timeout()"), lcd.display)

        self.timer.start(3000)
        
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Signal & slot')
        self.show()
        
def main():
    
    app = QtGui.QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()