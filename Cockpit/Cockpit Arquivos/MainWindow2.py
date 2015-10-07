# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow2.ui'
#
# Created: Mon Feb 03 15:53:20 2014
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
        MainWindow.resize(1280, 700)
        MainWindow.setWindowTitle(_fromUtf8("MainWindow"))
        MainWindow.setAutoFillBackground(False)
        MainWindow.setStyleSheet(_fromUtf8("background-image: url(:/backgroundImage/CockpitBackground.png);"))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.Compass = Qwt5.QwtCompass(self.centralwidget)
        self.Compass.setGeometry(QtCore.QRect(1060, 450, 200, 200))
        self.Compass.setLineWidth(4)
        self.Compass.setObjectName(_fromUtf8("Compass"))
        self.Compass_2 = Qwt5.QwtCompass(self.centralwidget)
        self.Compass_2.setGeometry(QtCore.QRect(1060, 100, 200, 200))
        self.Compass_2.setLineWidth(4)
        self.Compass_2.setObjectName(_fromUtf8("Compass_2"))
        self.Thermo = Qwt5.QwtThermo(self.centralwidget)
        self.Thermo.setGeometry(QtCore.QRect(360, 20, 711, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Thermo.setFont(font)
        self.Thermo.setAutoFillBackground(False)
        self.Thermo.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
""))
        self.Thermo.setInputMethodHints(QtCore.Qt.ImhNone)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.Thermo.setAlarmBrush(brush)
        self.Thermo.setAlarmColor(QtGui.QColor(255, 0, 0))
        self.Thermo.setAlarmEnabled(True)
        self.Thermo.setAlarmLevel(80.0)
        self.Thermo.setScalePosition(Qwt5.QwtThermo.TopScale)
        self.Thermo.setBorderWidth(3)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.Thermo.setFillBrush(brush)
        self.Thermo.setMaxValue(100.0)
        self.Thermo.setPipeWidth(20)
        self.Thermo.setProperty("value", 98.0)
        self.Thermo.setObjectName(_fromUtf8("Thermo"))
        self.frame = QtGui.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(20, 150, 281, 451))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.groupBoxInformacoes = QtGui.QGroupBox(self.frame)
        self.groupBoxInformacoes.setGeometry(QtCore.QRect(10, 200, 261, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBoxInformacoes.setFont(font)
        self.groupBoxInformacoes.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.groupBoxInformacoes.setTitle(_fromUtf8("Informações Internas"))
        self.groupBoxInformacoes.setObjectName(_fromUtf8("groupBoxInformacoes"))
        self.frameBussola = QtGui.QFrame(self.groupBoxInformacoes)
        self.frameBussola.setGeometry(QtCore.QRect(10, 170, 61, 71))
        self.frameBussola.setToolTip(_fromUtf8("Status GPS"))
        self.frameBussola.setStyleSheet(_fromUtf8("image: url(:/Icons/posicao.png);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.frameBussola.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameBussola.setFrameShadow(QtGui.QFrame.Raised)
        self.frameBussola.setObjectName(_fromUtf8("frameBussola"))
        self.lblTemp = QtGui.QLabel(self.groupBoxInformacoes)
        self.lblTemp.setGeometry(QtCore.QRect(10, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblTemp.setFont(font)
        self.lblTemp.setAutoFillBackground(False)
        self.lblTemp.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
""))
        self.lblTemp.setObjectName(_fromUtf8("lblTemp"))
        self.lblStatus = QtGui.QLabel(self.groupBoxInformacoes)
        self.lblStatus.setGeometry(QtCore.QRect(10, 100, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblStatus.setFont(font)
        self.lblStatus.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
""))
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        self.lblStatusValue = QtGui.QLabel(self.groupBoxInformacoes)
        self.lblStatusValue.setGeometry(QtCore.QRect(70, 120, 161, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.lblStatusValue.setFont(font)
        self.lblStatusValue.setStyleSheet(_fromUtf8("color: rgb(85, 255, 0);\n"
"\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.lblStatusValue.setTextFormat(QtCore.Qt.AutoText)
        self.lblStatusValue.setScaledContents(False)
        self.lblStatusValue.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblStatusValue.setWordWrap(False)
        self.lblStatusValue.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.lblStatusValue.setObjectName(_fromUtf8("lblStatusValue"))
        self.frameCamera = QtGui.QFrame(self.groupBoxInformacoes)
        self.frameCamera.setGeometry(QtCore.QRect(70, 170, 61, 71))
        self.frameCamera.setToolTip(_fromUtf8("Status Câmera"))
        self.frameCamera.setStyleSheet(_fromUtf8("image: url(:/Icons/camera1.png);\n"
"background-color: rgba(255, 255, 255, 0);\n"
""))
        self.frameCamera.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameCamera.setFrameShadow(QtGui.QFrame.Raised)
        self.frameCamera.setObjectName(_fromUtf8("frameCamera"))
        self.frameConexao = QtGui.QFrame(self.groupBoxInformacoes)
        self.frameConexao.setGeometry(QtCore.QRect(190, 170, 61, 71))
        self.frameConexao.setToolTip(_fromUtf8("Status Comunicação"))
        self.frameConexao.setStyleSheet(_fromUtf8("image: url(:/Icons/conexao.png);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.frameConexao.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameConexao.setFrameShadow(QtGui.QFrame.Raised)
        self.frameConexao.setObjectName(_fromUtf8("frameConexao"))
        self.frameFerramenta = QtGui.QFrame(self.groupBoxInformacoes)
        self.frameFerramenta.setGeometry(QtCore.QRect(130, 170, 61, 71))
        self.frameFerramenta.setToolTip(_fromUtf8("Status Atuadores"))
        self.frameFerramenta.setStyleSheet(_fromUtf8("image: url(:/Icons/ferramentas.png);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.frameFerramenta.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameFerramenta.setFrameShadow(QtGui.QFrame.Raised)
        self.frameFerramenta.setObjectName(_fromUtf8("frameFerramenta"))
        self.lblTemp_Value = QtGui.QLabel(self.groupBoxInformacoes)
        self.lblTemp_Value.setGeometry(QtCore.QRect(70, 50, 171, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.lblTemp_Value.setFont(font)
        self.lblTemp_Value.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.lblTemp_Value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTemp_Value.setObjectName(_fromUtf8("lblTemp_Value"))
        self.groupBox = QtGui.QGroupBox(self.frame)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 261, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.groupBox.setTitle(_fromUtf8("Informações Externas"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lblPressao_Value = QtGui.QLabel(self.groupBox)
        self.lblPressao_Value.setGeometry(QtCore.QRect(50, 135, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.lblPressao_Value.setFont(font)
        self.lblPressao_Value.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.lblPressao_Value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPressao_Value.setObjectName(_fromUtf8("lblPressao_Value"))
        self.lblPressao = QtGui.QLabel(self.groupBox)
        self.lblPressao.setGeometry(QtCore.QRect(10, 110, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblPressao.setFont(font)
        self.lblPressao.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
""))
        self.lblPressao.setObjectName(_fromUtf8("lblPressao"))
        self.lblTemp_Value_2 = QtGui.QLabel(self.groupBox)
        self.lblTemp_Value_2.setGeometry(QtCore.QRect(80, 50, 161, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.lblTemp_Value_2.setFont(font)
        self.lblTemp_Value_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.lblTemp_Value_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTemp_Value_2.setObjectName(_fromUtf8("lblTemp_Value_2"))
        self.lblTemp_2 = QtGui.QLabel(self.groupBox)
        self.lblTemp_2.setGeometry(QtCore.QRect(10, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblTemp_2.setFont(font)
        self.lblTemp_2.setAutoFillBackground(False)
        self.lblTemp_2.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
""))
        self.lblTemp_2.setObjectName(_fromUtf8("lblTemp_2"))
        self.videoPlayer = phonon.Phonon.VideoPlayer(self.centralwidget)
        self.videoPlayer.setGeometry(QtCore.QRect(340, 100, 701, 511))
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1280, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        self.lblTemp.setText(_translate("MainWindow", "Temperatura", None))
        self.lblStatus.setText(_translate("MainWindow", "Status", None))
        self.lblStatusValue.setText(_translate("MainWindow", "OK", None))
        self.lblTemp_Value.setText(_translate("MainWindow", "0.0 ºC", None))
        self.lblPressao_Value.setText(_translate("MainWindow", "0,00 m", None))
        self.lblPressao.setText(_translate("MainWindow", "Profundidade", None))
        self.lblTemp_Value_2.setText(_translate("MainWindow", "0.0 ºC", None))
        self.lblTemp_2.setText(_translate("MainWindow", "Temperatura", None))

from PyQt4 import phonon
from PyQt4 import Qwt5
import MainWindowBackgroundImage_rc
