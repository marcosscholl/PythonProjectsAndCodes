# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'VideoPlayer.ui'
#
# Created: Mon Jan 13 12:09:02 2014
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
        Form.resize(540, 426)
        self.videoPlayer = phonon.Phonon.VideoPlayer(Form)
        self.videoPlayer.setGeometry(QtCore.QRect(19, 9, 500, 380))
        self.videoPlayer.setObjectName(_fromUtf8("videoPlayer"))
        self.seekSlider = phonon.Phonon.SeekSlider(Form)
        self.seekSlider.setGeometry(QtCore.QRect(40, 400, 191, 19))
        self.seekSlider.setObjectName(_fromUtf8("seekSlider"))
        self.volumeSlider = phonon.Phonon.VolumeSlider(Form)
        self.volumeSlider.setGeometry(QtCore.QRect(340, 400, 141, 22))
        self.volumeSlider.setObjectName(_fromUtf8("volumeSlider"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))

from PyQt4 import phonon
