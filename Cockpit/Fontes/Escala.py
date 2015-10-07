# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 18:31:11 2014

@author: MarcosScholl
"""

if 0:
    import sip
    sip.settracemask(0x3f)

import math
import random
import sys
from PyQt4 import Qt, QtGui, QtCore
import PyQt4.Qwt5 as Qwt

# FAZ O TRATAMENTO PARA A LINGUAGEM
try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

# TRADUZ OS TEXTOS PARA O PADRÃO 
try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
        
        
def enumList(enum, sentinel):
    '''
    '''
    return [enum(i) for i in range(sentinel)]

colorGroupList = enumList(
    Qt.QPalette.ColorGroup, Qt.QPalette.NColorGroups)
colorRoleList = enumList(
    Qt.QPalette.ColorRole, Qt.QPalette.NColorRoles)
handList  = enumList(
    Qwt.QwtAnalogClock.Hand, Qwt.QwtAnalogClock.NHands)
    

class EscaleGrid(Qt.QFrame):

    def __init__(self, *args):
        Qt.QFrame.__init__(self, *args)
        palette = self.palette()
        #Cor Interna Bussola
        #palette.setColor(self.backgroundRole(), Qt.Qt.white)
        self.setPalette(palette)
        
        #Posicionamento do Widget
        layout = Qt.QGridLayout(self)
        layout.addWidget(self.__createThermo(1),1,1)
        layout.setColumnStretch(1,1)
        
    # __init__()
    
    def __createThermo(self, pos):

        palette = Qt.QPalette()
        for colorRole in colorRoleList:
            palette.setColor(colorRole, Qt.QColor())
        palette.setColor(
            Qt.QPalette.Base,
            #Alterando uma pouco a cor, mais forte ou mais fraco, depende do valor
            self.palette().color(self.backgroundRole()).light(105))
        palette.setColor(
            #Cor de fundo do corculo da agulha
            Qt.QPalette.Foreground,
            palette.color(Qt.QPalette.Base))
            
        #Fonte   
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setWeight(50)
        font.setStyle(Qt.QFont.s)
        
        # Criando Escala
        scale = Qwt.QwtThermo()
        scale.setGeometry(QtCore.QRect(70, 40, 91, 431))
        scale.setFont(font)  
        # Define Cor da escala, quando ultrapassar o limite
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        #Seta estas configurações para um alarma, da escala
        scale.setAlarmBrush(brush)
        scale.setAlarmColor(QtGui.QColor(255, 0, 0))
        #habilita o Alarme
        scale.setAlarmEnabled(True)
        #Define o Valor Limite, ate que o alarme seja habilitado
        scale.setAlarmLevel(80.0)
        # Define Posição da Escala
        scale.setScalePosition( Qwt.QwtThermo.TopScale)
        #scale.setOrientation(Qwt.QwtThermo.scalePosition()
        #Tamanho da borda da escala
        #scale.setBorderWidth(3)
        # Define a cor da escala padrão, quando ela nao esta acima do limite
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        # Ativa esse valor para a escala
        scale.setFillBrush(brush)
        # Define valor maximo da escala
        scale.setMaxValue(100)
        # Define largura da escala
        scale.setPipeWidth(21)
        # Pasa um valor para a escala
        scale.setValue(100.0)
        #scale.setProperty("value", 98.0)
        scale.setObjectName(_fromUtf8("Escala de Profundidade"))
        
        newPalette = scale.palette()
        
        scale.setPalette(newPalette)
        
        return scale



if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    av = EscaleGrid()
    
    av.setWindowFlags(Qt.Qt.FramelessWindowHint)
    av.setAttribute(Qt.Qt.WA_TranslucentBackground, True)
    av.setAttribute(Qt.Qt.WA_NoSystemBackground)
    av.setAutoFillBackground(False)
    av.setWindowOpacity(1)

    #av.setStyleSheet("background: transparent")
    
        
        
    av.setGeometry(220, 20, 800, 20)
    

    av.show()
    sys.exit(app.exec_()) 