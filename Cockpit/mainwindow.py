"""
This implements the Main Window.
"""
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from ui_mainwindow import *
import time

    
class MainWindow (QMainWindow, Ui_MainWindow):
    """A Simple Main Window"""
    
    def __init__(self, parent=None):
        """Constructor"""
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        #self.setStyleSheet("background-image: url(:/backgroundImage/CockpitBackground.png);")
        palette	= QPalette()
        palette.setBrush(QPalette.Background,QBrush(QPixmap("CockpitBackground.png")))
        self.setPalette(palette)

        
        
        #self.widgetHorizonte.setStyleSheet("background-color: rgba(255, 255, 255, 255);")
        #self.widgetBussola.update()
        print "antes"             
        """
        print "entrei"    
        aux = True
        while(aux):
            print "while"    
            print "Start : %s" % time.ctime()
        
            self.widgetHorizonte.setStyleSheet("background-color: rgba(255, 255, 255, 255);")
            self.widgetBussola.update()
            
            time.sleep( 5 )
            print "End : %s" % time.ctime()
            self.widgetHorizonte.setStyleSheet("background-color: rgba(255, 255, 255, 0);")
            self.widgetBussola.update()
            
            aux = False
        """
        
    def on_actionQuit_triggered(self):
        """Called automagically when the Quit menu entry is triggered"""
        exit()

