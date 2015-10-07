# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'informacoes.ui'
#
# Created: Tue Jan 14 12:00:14 2014
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

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.resize(178, 139)
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setEnabled(True)
        self.groupBox.setGeometry(QtCore.QRect(10, 0, 161, 131))
        self.groupBox.setSizeIncrement(QtCore.QSize(0, 0))
        self.groupBox.setBaseSize(QtCore.QSize(0, 0))
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.groupBox.setFont(font)
        self.groupBox.setMouseTracking(False)
        self.groupBox.setAutoFillBackground(True)
        self.groupBox.setInputMethodHints(QtCore.Qt.ImhNone)
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.groupBox.setCheckable(False)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lcdTemp = QtGui.QLCDNumber(self.groupBox)
        self.lcdTemp.setGeometry(QtCore.QRect(90, 20, 64, 23))
        self.lcdTemp.setObjectName(_fromUtf8("lcdTemp"))
        self.lblTemp = QtGui.QLabel(self.groupBox)
        self.lblTemp.setGeometry(QtCore.QRect(10, 30, 81, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblTemp.setFont(font)
        self.lblTemp.setObjectName(_fromUtf8("lblTemp"))
        self.lcdPressao = QtGui.QLCDNumber(self.groupBox)
        self.lcdPressao.setGeometry(QtCore.QRect(90, 50, 64, 23))
        self.lcdPressao.setObjectName(_fromUtf8("lcdPressao"))
        self.lblPressao = QtGui.QLabel(self.groupBox)
        self.lblPressao.setGeometry(QtCore.QRect(10, 60, 71, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lblPressao.setFont(font)
        self.lblPressao.setObjectName(_fromUtf8("lblPressao"))
        self.lblStatus = QtGui.QLabel(self.groupBox)
        self.lblStatus.setGeometry(QtCore.QRect(0, 80, 161, 20))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.lblStatus.setFont(font)
        self.lblStatus.setAlignment(QtCore.Qt.AlignCenter)
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        self.status = QtGui.QLabel(self.groupBox)
        self.status.setGeometry(QtCore.QRect(0, 100, 161, 21))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        font.setStyleStrategy(QtGui.QFont.PreferDefault)
        self.status.setFont(font)
        self.status.setStyleSheet(_fromUtf8("color: rgb(0, 0, 255);"))
        self.status.setTextFormat(QtCore.Qt.AutoText)
        self.status.setScaledContents(False)
        self.status.setAlignment(QtCore.Qt.AlignCenter)
        self.status.setWordWrap(False)
        self.status.setTextInteractionFlags(QtCore.Qt.NoTextInteraction)
        self.status.setObjectName(_fromUtf8("status"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.groupBox.setTitle(_translate("Form", "Informações:", None))
        self.lblTemp.setText(_translate("Form", "Temperatura:", None))
        self.lblPressao.setText(_translate("Form", "Pressão:", None))
        self.lblStatus.setText(_translate("Form", "Status:", None))
        self.status.setText(_translate("Form", "OK", None))

