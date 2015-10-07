# -*- coding: utf-8 -*-
"""
Created on Sat Dec 14 11:41:48 2013

@author: MarcosScholl
"""

from PyQt4 import QtGui, QtCore
from VideoPlayer import Ui_Form
#from mainwindow import Ui_MainWindow

class MinhaClasse(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    av = MinhaClasse()
    av.show()
    sys.exit(app.exec_())
    