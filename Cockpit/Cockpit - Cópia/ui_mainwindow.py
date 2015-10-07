# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Tue Feb 04 00:15:53 2014
#      by: PyQt4 UI code generator 4.9.6
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1280, 800)
        #MainWindow.setStyleSheet(_fromUtf8("background-image: url(:/backgroundImage/CockpitBackground.png);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frameWindow = QtGui.QFrame(self.centralwidget)
        self.frameWindow.setGeometry(QtCore.QRect(0, 0, 1280, 800))
        self.frameWindow.setAutoFillBackground(False)
        self.frameWindow.setStyleSheet(_fromUtf8(""))
        self.frameWindow.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameWindow.setFrameShadow(QtGui.QFrame.Raised)
        self.frameWindow.setObjectName(_fromUtf8("frameWindow"))
        self.frameEscala = QtGui.QFrame(self.frameWindow)
        self.frameEscala.setGeometry(QtCore.QRect(0, 0, 1281, 81))
        self.frameEscala.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameEscala.setFrameShadow(QtGui.QFrame.Raised)
        self.frameEscala.setObjectName(_fromUtf8("frameEscala"))
        self.verticalLayout = QtGui.QVBoxLayout(self.frameEscala)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setMargin(0)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.escalegrid = EscaleGrid(self.frameEscala)
        self.escalegrid.setObjectName(_fromUtf8("escalegrid"))
        self.verticalLayout.addWidget(self.escalegrid)
        self.frameHealth = QtGui.QFrame(self.frameWindow)
        self.frameHealth.setGeometry(QtCore.QRect(10, 190, 272, 448))
        self.frameHealth.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0.017, stop:0.0451977 rgba(0, 0, 40, 255), stop:1 rgba(0, 0, 141, 255));"))
        self.frameHealth.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameHealth.setFrameShadow(QtGui.QFrame.Raised)
        self.frameHealth.setObjectName(_fromUtf8("frameHealth"))
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.frameHealth)
        self.verticalLayout_2.setMargin(0)
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.healthWidget = HealthWidget(self.frameHealth)
        self.healthWidget.setObjectName(_fromUtf8("healthWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.healthWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_2.addWidget(self.healthWidget)
        self.frameBussola = QtGui.QFrame(self.frameWindow)
        self.frameBussola.setGeometry(QtCore.QRect(1040, 190, 241, 241))
        self.frameBussola.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameBussola.setFrameShadow(QtGui.QFrame.Raised)
        self.frameBussola.setObjectName(_fromUtf8("frameBussola"))
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frameBussola)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setMargin(0)
        self.verticalLayout_4.setObjectName(_fromUtf8("verticalLayout_4"))
        self.widgetBussola = WidgetBussola(self.frameBussola)
        self.widgetBussola.setObjectName(_fromUtf8("widgetBussola"))
        self.verticalLayout_4.addWidget(self.widgetBussola)
        self.frameHorizonte = QtGui.QFrame(self.frameWindow)
        self.frameHorizonte.setGeometry(QtCore.QRect(1040, 440, 241, 241))
        self.frameHorizonte.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameHorizonte.setFrameShadow(QtGui.QFrame.Raised)
        self.frameHorizonte.setObjectName(_fromUtf8("frameHorizonte"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.frameHorizonte)
        self.verticalLayout_5.setSpacing(0)
        self.verticalLayout_5.setMargin(0)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.widgetHorizonte = HorizonArtifictialWidget(self.frameHorizonte)
        self.widgetHorizonte.setObjectName(_fromUtf8("widgetHorizonte"))
        self.verticalLayout_5.addWidget(self.widgetHorizonte)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))

from healthWidget import HealthWidget
from escalegrid import EscaleGrid
from widgetBussola import WidgetBussola
from horizonArtifictialWidget import HorizonArtifictialWidget
import MainWindowBackgroundImage_rc
