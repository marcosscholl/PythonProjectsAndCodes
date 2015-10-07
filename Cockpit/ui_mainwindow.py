# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created: Thu Feb 06 12:31:06 2014
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
        MainWindow.resize(1270, 790)
        MainWindow.setWindowTitle(_fromUtf8("MainWindow"))
        MainWindow.setToolTip(_fromUtf8(""))
        MainWindow.setStatusTip(_fromUtf8(""))
        MainWindow.setWhatsThis(_fromUtf8(""))
        MainWindow.setStyleSheet(_fromUtf8(""))
        MainWindow.setWindowFilePath(_fromUtf8(""))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setToolTip(_fromUtf8(""))
        self.centralwidget.setStatusTip(_fromUtf8(""))
        self.centralwidget.setWhatsThis(_fromUtf8(""))
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.frameWindow = QtGui.QFrame(self.centralwidget)
        self.frameWindow.setGeometry(QtCore.QRect(0, 0, 1270, 790))
        self.frameWindow.setToolTip(_fromUtf8(""))
        self.frameWindow.setStatusTip(_fromUtf8(""))
        self.frameWindow.setWhatsThis(_fromUtf8(""))
        self.frameWindow.setAutoFillBackground(False)
        self.frameWindow.setStyleSheet(_fromUtf8(""))
        self.frameWindow.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameWindow.setFrameShadow(QtGui.QFrame.Raised)
        self.frameWindow.setLineWidth(0)
        self.frameWindow.setObjectName(_fromUtf8("frameWindow"))
        self.frameEscala = QtGui.QFrame(self.frameWindow)
        self.frameEscala.setGeometry(QtCore.QRect(0, 0, 1281, 81))
        self.frameEscala.setToolTip(_fromUtf8(""))
        self.frameEscala.setStatusTip(_fromUtf8(""))
        self.frameEscala.setWhatsThis(_fromUtf8(""))
        self.frameEscala.setStyleSheet(_fromUtf8(""))
        self.frameEscala.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameEscala.setFrameShadow(QtGui.QFrame.Raised)
        self.frameEscala.setLineWidth(0)
        self.frameEscala.setObjectName(_fromUtf8("frameEscala"))
        self.verticalLayout_Escala = QtGui.QVBoxLayout(self.frameEscala)
        self.verticalLayout_Escala.setSpacing(0)
        self.verticalLayout_Escala.setMargin(0)
        self.verticalLayout_Escala.setObjectName(_fromUtf8("verticalLayout_Escala"))
        self.escalegrid = EscaleGrid(self.frameEscala)
        self.escalegrid.setToolTip(_fromUtf8(""))
        self.escalegrid.setStatusTip(_fromUtf8(""))
        self.escalegrid.setWhatsThis(_fromUtf8(""))
        self.escalegrid.setStyleSheet(_fromUtf8(""))
        self.escalegrid.setObjectName(_fromUtf8("escalegrid"))
        self.verticalLayout_Escala.addWidget(self.escalegrid)
        self.frameHealth = QtGui.QFrame(self.frameWindow)
        self.frameHealth.setGeometry(QtCore.QRect(10, 190, 272, 448))
        self.frameHealth.setToolTip(_fromUtf8(""))
        self.frameHealth.setStatusTip(_fromUtf8(""))
        self.frameHealth.setWhatsThis(_fromUtf8(""))
        self.frameHealth.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0.017, stop:0.0451977 rgba(0, 0, 40, 255), stop:1 rgba(0, 0, 141, 255));"))
        self.frameHealth.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameHealth.setFrameShadow(QtGui.QFrame.Raised)
        self.frameHealth.setLineWidth(0)
        self.frameHealth.setObjectName(_fromUtf8("frameHealth"))
        self.verticalLayout_Health = QtGui.QVBoxLayout(self.frameHealth)
        self.verticalLayout_Health.setMargin(0)
        self.verticalLayout_Health.setObjectName(_fromUtf8("verticalLayout_Health"))
        self.healthWidget = HealthWidget(self.frameHealth)
        self.healthWidget.setToolTip(_fromUtf8(""))
        self.healthWidget.setStatusTip(_fromUtf8(""))
        self.healthWidget.setWhatsThis(_fromUtf8(""))
        self.healthWidget.setStyleSheet(_fromUtf8(""))
        self.healthWidget.setObjectName(_fromUtf8("healthWidget"))
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.healthWidget)
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.verticalLayout_Health.addWidget(self.healthWidget)
        self.frameBussola = QtGui.QFrame(self.frameWindow)
        self.frameBussola.setGeometry(QtCore.QRect(1040, 190, 241, 241))
        self.frameBussola.setToolTip(_fromUtf8(""))
        self.frameBussola.setStatusTip(_fromUtf8(""))
        self.frameBussola.setWhatsThis(_fromUtf8(""))
        self.frameBussola.setStyleSheet(_fromUtf8(""))
        self.frameBussola.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameBussola.setFrameShadow(QtGui.QFrame.Raised)
        self.frameBussola.setLineWidth(0)
        self.frameBussola.setObjectName(_fromUtf8("frameBussola"))
        self.verticalLayout_Bussola = QtGui.QVBoxLayout(self.frameBussola)
        self.verticalLayout_Bussola.setSpacing(0)
        self.verticalLayout_Bussola.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.verticalLayout_Bussola.setMargin(0)
        self.verticalLayout_Bussola.setObjectName(_fromUtf8("verticalLayout_Bussola"))
        self.widgetBussola = WidgetBussola(self.frameBussola)
        self.widgetBussola.setToolTip(_fromUtf8(""))
        self.widgetBussola.setStatusTip(_fromUtf8(""))
        self.widgetBussola.setWhatsThis(_fromUtf8(""))
        self.widgetBussola.setStyleSheet(_fromUtf8(""))
        self.widgetBussola.setObjectName(_fromUtf8("widgetBussola"))
        self.widgetBussola.setGeometry(1040, 190, 241, 241)
        self.verticalLayout_Bussola.addWidget(self.widgetBussola)
       
        bussola = WidgetBussola;
       
        self.frameHorizonte = QtGui.QFrame(self.frameWindow)
        self.frameHorizonte.setGeometry(QtCore.QRect(1040, 440, 241, 241))
        self.frameHorizonte.setToolTip(_fromUtf8(""))
        self.frameHorizonte.setStatusTip(_fromUtf8(""))
        self.frameHorizonte.setWhatsThis(_fromUtf8(""))
        self.frameHorizonte.setStyleSheet(_fromUtf8(""))
        self.frameHorizonte.setFrameShape(QtGui.QFrame.NoFrame)
        self.frameHorizonte.setFrameShadow(QtGui.QFrame.Raised)
        self.frameHorizonte.setLineWidth(0)
        self.frameHorizonte.setObjectName(_fromUtf8("frameHorizonte"))
        self.verticalLayout_Horizonte = QtGui.QVBoxLayout(self.frameHorizonte)
        self.verticalLayout_Horizonte.setSpacing(0)
        self.verticalLayout_Horizonte.setMargin(0)
        self.verticalLayout_Horizonte.setObjectName(_fromUtf8("verticalLayout_Horizonte"))
        self.widgetHorizonte = HorizonArtifictialWidget(self.frameHorizonte)
        self.widgetHorizonte.setToolTip(_fromUtf8(""))
        self.widgetHorizonte.setStatusTip(_fromUtf8(""))
        self.widgetHorizonte.setWhatsThis(_fromUtf8(""))
        self.widgetHorizonte.setStyleSheet(_fromUtf8(""))
        self.widgetHorizonte.setObjectName(_fromUtf8("widgetHorizonte"))
        self.verticalLayout_Horizonte.addWidget(self.widgetHorizonte)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1270, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        #self.widgetBussola.ui
        
        
        
    def retranslateUi(self, MainWindow):
        pass

from healthWidget import HealthWidget
from escalegrid import EscaleGrid
from widgetBussola import WidgetBussola
from horizonArtifictialWidget import HorizonArtifictialWidget
import MainWindowBackgroundImage_rc
