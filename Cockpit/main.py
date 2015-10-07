

"""
This is the main program.
"""

from PyQt4.QtCore import *
from PyQt4.QtGui import *
import mainwindow
import sys
from ui_mainwindow import Ui_MainWindow

app = QApplication(sys.argv)
form = mainwindow.MainWindow ()



form.show()
app.exec_()

