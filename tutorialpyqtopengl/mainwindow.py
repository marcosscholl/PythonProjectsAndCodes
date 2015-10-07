"""
This implements the Main Window.
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_mainwindow import *
    
class MainWindow (QMainWindow, Ui_MainWindow):
    """A Simple Main Window"""
    
    def __init__(self, parent=None):
        """Constructor"""
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        
    def on_actionQuit_triggered(self):
        """Called automagically when the Quit menu entry is triggered"""
        exit()

