# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 16:20:33 2014

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
    
"""
def __colorTheme(self, base):
        background = base.dark(150)
        foreground = base.dark(200)
        
        mid = base.dark(110)
        dark = base.dark(170)
        light = base.light(170)
        text = foreground.light(800)

        palette = Qt.QPalette()
        for colorGroup in colorGroupList:
            palette.setColor(colorGroup, Qt.QPalette.Base, base)
            palette.setColor(colorGroup, Qt.QPalette.Background, background)
            palette.setColor(colorGroup, Qt.QPalette.Mid, mid)
            palette.setColor(colorGroup, Qt.QPalette.Light, light)
            palette.setColor(colorGroup, Qt.QPalette.Dark, dark)
            palette.setColor(colorGroup, Qt.QPalette.Text, text)
            palette.setColor(colorGroup, Qt.QPalette.Foreground, foreground)
    
        return palette
"""

class CompassGrid(Qt.QFrame):

    def __init__(self, *args):
        Qt.QFrame.__init__(self, *args)

        palette = self.palette()
        #Cor Interna Bussola
        palette.setColor(self.backgroundRole(), Qt.Qt.darkCyan)
        self.setPalette(palette)
        
        #Posicionamento do Widget
        layout = Qt.QGridLayout(self)
        layout.addWidget(self.__createCompass(1),1,1)
        layout.setColumnStretch(1,1)
        
    # __init__()
    
    def __createCompass(self, pos):

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

        compass = Qwt.QwtCompass()
               
        #linhaBorda
        compass.setLineWidth(2)
      
        
            
        #compass.setFrameShadow(Qwt.QwtCompass.Sunken)  //Plain    
        compass.setFrameShadow(Qwt.QwtCompass.Raised)
        compass.setScaleTicks(0, 0, 2)
       
        compass.setScaleOptions( Qwt.QwtDial.ScaleTicks |  Qwt.QwtDial.ScaleLabel | 
            Qwt.QwtDial.ScaleBackbone)
        compass.setLabelMap({0.0: "N",
                                 45.0: "ne",
                                 90.0: "E",
                                 135.0: "se",
                                 180.0: "S",
                                 225.0: "so",
                                 270.0: "O",
                                 315.0: "no"})
        compass.setScale(72,0, 0)

        # QwtCompassMagnetNeedle =A agulha da bússola ímã para widgets
        compass.setNeedle(Qwt.QwtCompassMagnetNeedle(
        Qwt.QwtCompassMagnetNeedle.TriangleStyle,
            Qt.Qt.white,
            Qt.Qt.red))
        compass.setValue(35.0)
        compass.setToolTip("Bussola_3")
        
        
        #Dando cor a Bussola
        newPalette = compass.palette()
    
        
        ##Criando Cor de fundo para Bussola
        
        for colorRole in colorRoleList:
            if palette.color(colorRole).isValid():
                for colorGroup in colorGroupList:
                    newPalette.setColor(
                        colorGroup, colorRole, palette.color(colorRole))
        
        

            #newPalette.setColor(colorGroup, Qt.QPalette.Dark, dark)
            #newPalette.setColor(colorGroup, Qt.QPalette.Mid, mid)
            #newPalette.setColor(colorGroup, Qt.QPalette.Light, light)

        compass.setPalette(newPalette)

        return compass

    # __createCompass()

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    av = CompassGrid()
    
    
    """
    QtCore.Qt.Window | QtCore.Qt.WindowTitleHint | QtCore.Qt.CustomizeWindowHint
    """
    #av.setWindowFlags( Qt.Qt.CustomizeWindowHint)
    #av.setAttribute(Qt.Qt.WA_TranslucentBackground, True)
    #av.setAttribute(Qt.Qt.WA_NoSystemBackground)
    #av.setAutoFillBackground(False)
    #av.setWindowOpacity(1)

    #av.setStyleSheet("background: transparent")
       
    av.setGeometry(1050, 100, 300, 300)
    
    #av.setAutoFillBackground(False)

    av.show()
    sys.exit(app.exec_()) 