# -*- coding: utf-8 -*-
"""
Created on Mon Feb 03 15:44:16 2014

@author: MarcosScholl
"""


from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt
from MainWindow2 import Ui_MainWindow
#from mainwindow import Ui_MainWindow

class MinhaClasse(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    av = MinhaClasse()
    #av.setStyleSheet("background: transparent")
    
    av.show()
    sys.exit(app.exec_())
    