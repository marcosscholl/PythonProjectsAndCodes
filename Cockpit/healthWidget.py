"""
Created on Tue Fev 03 18:49:43 2014

@author: MarcosScholl
"""

from PyQt4 import Qt, QtGui, QtCore
import PyQt4.Qwt5 as Qwt
import IconsHealth_rc       


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
        
class CriaHealth(Qt.QFrame):
      
    def setupUi(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowModality(QtCore.Qt.NonModal)
        Form.resize(272, 448)
        Form.setLayoutDirection(QtCore.Qt.LeftToRight)
        Form.setAutoFillBackground(False)
        Form.setStyleSheet(_fromUtf8("background-color: qlineargradient(spread:pad, x1:0.5, y1:1, x2:0.5, y2:0.017, stop:0.0451977 rgba(0, 0, 40, 255), stop:1 rgba(0, 0, 141, 255));\n"
"\n"
""))
        Form.setWindowFilePath(_fromUtf8(""))
        Form.setInputMethodHints(QtCore.Qt.ImhNone)
        self.groupBoxInformacoes = QtGui.QGroupBox(Form)
        self.groupBoxInformacoes.setGeometry(QtCore.QRect(5, 200, 261, 241))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBoxInformacoes.setFont(font)
        self.groupBoxInformacoes.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        self.groupBoxInformacoes.setTitle(_fromUtf8("Informacoes Internas"))
        self.groupBoxInformacoes.setObjectName(_fromUtf8("groupBoxInformacoes"))
        self.frameBussola = QtGui.QFrame(self.groupBoxInformacoes)
        self.frameBussola.setGeometry(QtCore.QRect(10, 170, 61, 71))
        self.frameBussola.setToolTip(_fromUtf8("Status GPS"))
        self.frameBussola.setStyleSheet(_fromUtf8("image: url(:/Icons/posicao.png);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.frameBussola.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameBussola.setFrameShadow(QtGui.QFrame.Raised)
        self.frameBussola.setObjectName(_fromUtf8("frameBussola"))
        self.lblTemp_Int = QtGui.QLabel(self.groupBoxInformacoes)
        self.lblTemp_Int.setGeometry(QtCore.QRect(10, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblTemp_Int.setFont(font)
        self.lblTemp_Int.setAutoFillBackground(False)
        self.lblTemp_Int.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
""))
        self.lblTemp_Int.setObjectName(_fromUtf8("lblTemp_Int"))
        self.lblStatus = QtGui.QLabel(self.groupBoxInformacoes)
        self.lblStatus.setGeometry(QtCore.QRect(10, 100, 111, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblStatus.setFont(font)
        self.lblStatus.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
""))
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        self.lblStatusValue = QtGui.QLabel(self.groupBoxInformacoes)
        self.lblStatusValue.setGeometry(QtCore.QRect(50, 120, 181, 41))
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
        self.frameCamera.setToolTip(_fromUtf8("Status Camera"))
        self.frameCamera.setStyleSheet(_fromUtf8("image: url(:/Icons/camera1.png);\n"
"background-color: rgba(255, 255, 255, 0);\n"
""))
        self.frameCamera.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameCamera.setFrameShadow(QtGui.QFrame.Raised)
        self.frameCamera.setObjectName(_fromUtf8("frameCamera"))
        self.frameConexao = QtGui.QFrame(self.groupBoxInformacoes)
        self.frameConexao.setGeometry(QtCore.QRect(190, 170, 61, 71))
        self.frameConexao.setToolTip(_fromUtf8("Status Comunicacao"))
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
        self.lblTemp_Int_Value = QtGui.QLabel(self.groupBoxInformacoes)
        self.lblTemp_Int_Value.setGeometry(QtCore.QRect(50, 50, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.lblTemp_Int_Value.setFont(font)
        self.lblTemp_Int_Value.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.lblTemp_Int_Value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTemp_Int_Value.setObjectName(_fromUtf8("lblTemp_Int_Value"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(5, 0, 261, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);"))
        self.groupBox.setTitle(_fromUtf8("Informacoes Externas"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lblProfundidade_Value = QtGui.QLabel(self.groupBox)
        self.lblProfundidade_Value.setGeometry(QtCore.QRect(40, 135, 201, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.lblProfundidade_Value.setFont(font)
        self.lblProfundidade_Value.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.lblProfundidade_Value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblProfundidade_Value.setObjectName(_fromUtf8("lblProfundidade_Value"))
        self.lblProfundidade = QtGui.QLabel(self.groupBox)
        self.lblProfundidade.setGeometry(QtCore.QRect(10, 110, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblProfundidade.setFont(font)
        self.lblProfundidade.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
""))
        self.lblProfundidade.setObjectName(_fromUtf8("lblProfundidade"))
        self.lblTemp_Ext_Value = QtGui.QLabel(self.groupBox)
        self.lblTemp_Ext_Value.setGeometry(QtCore.QRect(50, 50, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.lblTemp_Ext_Value.setFont(font)
        self.lblTemp_Ext_Value.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.lblTemp_Ext_Value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTemp_Ext_Value.setObjectName(_fromUtf8("lblTemp_Ext_Value"))
        self.lblTemp_Ext = QtGui.QLabel(self.groupBox)
        self.lblTemp_Ext.setGeometry(QtCore.QRect(10, 20, 211, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblTemp_Ext.setFont(font)
        self.lblTemp_Ext.setAutoFillBackground(False)
        self.lblTemp_Ext.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
""))
        self.lblTemp_Ext.setObjectName(_fromUtf8("lblTemp_Ext"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lblTemp_Int.setText(_translate("Form", "Temperatura", None))
        self.lblStatus.setText(_translate("Form", "Status", None))
        self.lblStatusValue.setText(_translate("Form", "OK", None))
        self.lblTemp_Int_Value.setText(_translate("Form", "0.0 C", None))
        self.lblProfundidade_Value.setText(_translate("Form", "0,00 m", None))
        self.lblProfundidade.setText(_translate("Form", "Profundidade", None))
        self.lblTemp_Ext_Value.setText(_translate("Form", "0.0 C", None))
        self.lblTemp_Ext.setText(_translate("Form", "Temperatura", None))
        
    def mousePressEvent(self, QMouseEvent):
        anterior = 0
        
        cursor =QtGui.QCursor(self)
        position = QMouseEvent.pos()
        xpos = QMouseEvent.x()
        ypos = QMouseEvent.y()

        print QMouseEvent.pos()
        
        if (anterior != QMouseEvent.pos()):
            anterior = QMouseEvent.pos()
            self.frameBussola.setStyleSheet(_fromUtf8("image: url(:/Icons/menu_bt_navigation2.png);\n"
""))
        


class HealthWidget(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)
        self.ui = CriaHealth()
        self.ui.setupUi(self) 
        
        #self.setGeometry(300, 10, 725, 70)
        