# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'QwtTermo.ui'
#
# Created: Wed Dec 18 10:06:48 2013
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
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(288, 512)
        font = QtGui.QFont()
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        Form.setFont(font)
        Form.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        Form.setAcceptDrops(False)
        Form.setWhatsThis(_fromUtf8(""))
        Form.setLayoutDirection(QtCore.Qt.RightToLeft)
        Form.setAutoFillBackground(False)
        Form.setInputMethodHints(QtCore.Qt.ImhPreferUppercase)
        self.Thermo = Qwt5.QwtThermo(Form)
        self.Thermo.setGeometry(QtCore.QRect(70, 40, 91, 431))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(False)
        font.setWeight(50)
        self.Thermo.setFont(font)
        self.Thermo.setAutoFillBackground(False)
        self.Thermo.setInputMethodHints(QtCore.Qt.ImhNone)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.Dense1Pattern)
        self.Thermo.setAlarmBrush(brush)
        self.Thermo.setAlarmColor(QtGui.QColor(255, 0, 0))
        self.Thermo.setAlarmEnabled(True)
        self.Thermo.setAlarmLevel(80.0)
        self.Thermo.setScalePosition(Qwt5.QwtThermo.LeftScale)
        self.Thermo.setBorderWidth(3)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.Dense1Pattern)
        self.Thermo.setFillBrush(brush)
        self.Thermo.setMaxValue(100.0)
        self.Thermo.setPipeWidth(20)
        self.Thermo.setProperty("value", 98.0)
        self.Thermo.setObjectName(_fromUtf8("Thermo"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

from PyQt4 import Qwt5
