# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'simulator_ui.ui'
#
# Created: Mon Mar 09 22:34:04 2015
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

class Ui_Ui_main(object):
    def setupUi(self, Ui_main):
        Ui_main.setObjectName(_fromUtf8("Ui_main"))
        Ui_main.resize(412, 270)
        self.txtNPart = QtGui.QLineEdit(Ui_main)
        self.txtNPart.setGeometry(QtCore.QRect(270, 30, 131, 27))
        self.txtNPart.setInputMask(_fromUtf8(""))
        self.txtNPart.setText(_fromUtf8("100"))
        self.txtNPart.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtNPart.setObjectName(_fromUtf8("txtNPart"))
        self.label = QtGui.QLabel(Ui_main)
        self.label.setGeometry(QtCore.QRect(270, 10, 141, 17))
        self.label.setText(_fromUtf8("Number of Particles"))
        self.label.setObjectName(_fromUtf8("label"))
        self.frame = QtGui.QFrame(Ui_main)
        self.frame.setGeometry(QtCore.QRect(10, 10, 250, 250))
        self.frame.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtGui.QFrame.Raised)
        self.frame.setObjectName(_fromUtf8("frame"))
        self.btnSetup = QtGui.QPushButton(Ui_main)
        self.btnSetup.setGeometry(QtCore.QRect(340, 60, 61, 27))
        self.btnSetup.setText(_fromUtf8("Setup"))
        self.btnSetup.setObjectName(_fromUtf8("btnSetup"))
        self.btnRun = QtGui.QPushButton(Ui_main)
        self.btnRun.setGeometry(QtCore.QRect(340, 230, 61, 27))
        self.btnRun.setText(_fromUtf8("Run"))
        self.btnRun.setObjectName(_fromUtf8("btnRun"))
        self.txtNSteps = QtGui.QLineEdit(Ui_main)
        self.txtNSteps.setGeometry(QtCore.QRect(270, 200, 131, 27))
        self.txtNSteps.setInputMask(_fromUtf8(""))
        self.txtNSteps.setText(_fromUtf8("1000"))
        self.txtNSteps.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txtNSteps.setObjectName(_fromUtf8("txtNSteps"))
        self.label_2 = QtGui.QLabel(Ui_main)
        self.label_2.setGeometry(QtCore.QRect(270, 180, 131, 17))
        self.label_2.setText(_fromUtf8("Number of Steps"))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        self.retranslateUi(Ui_main)
        QtCore.QMetaObject.connectSlotsByName(Ui_main)

    def retranslateUi(self, Ui_main):
        Ui_main.setWindowTitle(_translate("Ui_main", "Simulator", None))

