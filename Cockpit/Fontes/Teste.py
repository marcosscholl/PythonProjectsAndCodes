# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 14:30:51 2014

@author: MarcosScholl
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 10:14:32 2013

@author: MarcosScholl
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 09:44:06 2013

@author: MarcosScholl
"""

# The Python version of qwt-*/examples/dials

# for debugging, requires: python configure.py --trace ...
if 0:
    import sip
    sip.settracemask(0x3f)

import math
import random
import sys
from PyQt4 import Qt, QtGui
import PyQt4.Qwt5 as Qwt


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


class CompassGrid(Qt.QFrame):

    def __init__(self, *args):
        Qt.QFrame.__init__(self, *args)

        palette = self.palette()
        #Cor Interna Bussola
        
        palette.setColor(self.backgroundRole(), Qt.Qt.darkCyan)
        #self.setPalette(palette)
       
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

        #compass.setColor(Qt.Qt.red)
        #compass.setPalette(newPalette)
        return compass

    # __createCompass()

            



"""
def make():
    demo = Qt.QTabWidget()
    demo.addTab(CompassGrid(), "Compass")
    demo.show()
    return demo

# make()


def main(args):
    app = Qt.QApplication(args)
    demo = make()
    sys.exit(app.exec_())
"""
# main()


# Admire!
#if __name__ == '__main__':
"""
    if 'settracemask' in sys.argv:
        # for debugging, requires: python configure.py --trace ...
        import sip
        sip.settracemask(0x3f)

    main(sys.argv)
"""

if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    av = CompassGrid()
    av.show()
    sys.exit(app.exec_())
    
# Local Variables: ***
# mode: python ***
# End: ***