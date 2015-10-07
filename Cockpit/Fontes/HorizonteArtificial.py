# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 08:31:06 2013

@author: MarcosScholl
"""

if 0:
    import sip
    sip.settracemask(0x3f)

import math
import random
import sys
from PyQt4 import Qt
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
    
    
    
"""
class SpeedoMeter(Qwt.QwtDial):

    def __init__(self, *args):
        Qwt.QwtDial.__init__(self, *args)
        self.__label = 'km/h'
        self.setWrapping(False)
        self.setReadOnly(True)

        self.setOrigin(135.0)
        self.setScaleArc(0.0, 270.0)

        self.setNeedle(Qwt.QwtDialSimpleNeedle(
            Qwt.QwtDialSimpleNeedle.Arrow,
            True,
            Qt.QColor(Qt.Qt.red),
            Qt.QColor(Qt.Qt.gray).light(130)))

        self.setScaleOptions(Qwt.QwtDial.ScaleTicks | Qwt.QwtDial.ScaleLabel)
        self.setScaleTicks(0, 4, 8)

    # __init__()
    
    def setLabel(self, text):
        self.__label = text
        self.update()

    # setLabel()
    
    def label(self):
        return self.__label

    # label()
    
    def drawScaleContents(self, painter, center, radius):
        rect = Qt.QRect(0, 0, 2 * radius, 2 * radius - 10)
        rect.moveCenter(center)
        painter.setPen(self.palette().color(Qt.QPalette.Text))
        painter.drawText(
            rect, Qt.Qt.AlignBottom | Qt.Qt.AlignHCenter, self.__label)

    # drawScaleContents

# class SpeedoMeter
"""

class AttitudeIndicatorNeedle(Qwt.QwtDialNeedle):

    def __init__(self, color):
        Qwt.QwtDialNeedle.__init__(self)
        palette = Qt.QPalette()
        for colourGroup in colorGroupList:
            ## Cor dos Indicadores QtGui.QColor(255, 0, 0)
            palette.setColor(colourGroup, Qt.QPalette.Text, color)
        self.setPalette(palette)

    # __init__()

    def draw(self, painter, center, length, direction, cg):
        direction *= math.pi / 180.0
        triangleSize = int(round(length * 0.1))

        painter.save()

        p0 = Qt.QPoint(center.x() + 1, center.y() + 1)
        p1 = Qwt.qwtPolar2Pos(p0, length - 2 * triangleSize - 2, direction)

        pa = Qt.QPolygon([
            Qwt.qwtPolar2Pos(p1, 2 * triangleSize, direction),
            Qwt.qwtPolar2Pos(p1, triangleSize, direction + math.pi/2),
            Qwt.qwtPolar2Pos(p1, triangleSize, direction - math.pi/2),
            ])

        color = self.palette().color(cg, Qt.QPalette.Text)
        painter.setBrush(color)
        painter.drawPolygon(pa)

        painter.setPen(Qt.QPen(color, 3))
        painter.drawLine(
            Qwt.qwtPolar2Pos(p0, length - 2, direction + math.pi/2),
            Qwt.qwtPolar2Pos(p0, length - 2, direction - math.pi/2))

        painter.restore()

    # draw()

# class AttitudeIndicatorNeedle


class AttitudeIndicator(Qwt.QwtDial):

    def __init__(self, *args):
        Qwt.QwtDial.__init__(self, *args)
        self.__gradient = 0.0
        self.setMode(Qwt.QwtDial.RotateScale)
        self.setWrapping(True)
        self.setOrigin(270.0)
        self.setScaleOptions(Qwt.QwtDial.ScaleTicks)
        self.setScale(0, 0, 30.0)
        self.setNeedle(AttitudeIndicatorNeedle(
            self.palette().color(Qt.QPalette.Text)))
            

    # __init__()

    def angle(self):
        return self.value()

    # angle()
    
    def setAngle(self, angle):
        self.setValue(angle)

    # setAngle()

    def gradient(self):
        return self.__gradient

    # gradient()

    def setGradient(self, gradient):
        self.__gradient = gradient

    # setGradient()
    
    def keyPressEvent(self, event):
        if event.key() == Qt.Qt.Key_Plus:
            self.setGradient(self.gradient() + 0.05)
        elif event.key() == Qt.Qt.Key_Minus:
            self.setGradient(self.gradient() - 0.05)
        else:
            Qwt.QwtDial.keyPressEvent(self, event)

    # keyPressEvent()
    # Faz a Escala de Angulação  acompanhar a rotação do horizonte
    def drawScale(self, painter, center, radius, origin, minArc, maxArc):
        dir = (360.0 - origin) * math.pi / 180.0
        offset = 4
        p0 = Qwt.qwtPolar2Pos(center, offset, dir + math.pi)

        w = self.contentsRect().width()

        # clip region to swallow 180 - 360 degrees
        pa = []
        pa.append(Qwt.qwtPolar2Pos(p0, w, dir - math.pi/2))
        pa.append(Qwt.qwtPolar2Pos(pa[-1], 2 * w, dir + math.pi/2))
        pa.append(Qwt.qwtPolar2Pos(pa[-1], w, dir))
        pa.append(Qwt.qwtPolar2Pos(pa[-1], 2 * w, dir - math.pi/2))

        painter.save()
        painter.setClipRegion(Qt.QRegion(Qt.QPolygon(pa)))
        
        Qwt.QwtDial.drawScale(
            self, painter, center, radius, origin, minArc, maxArc)
        painter.restore()
    
    # drawScale()
    # Cria o Horizonte.
    def drawScaleContents(self, painter, center, radius):
        # Cria a escala azul
        ############################################################
        dir = 360 - int(round(self.origin() - self.value()))
        arc = 90 + int(round(self.gradient() * 90))
        skyColor = Qt.QColor(38, 151, 221)
        painter.save()
        painter.setBrush(skyColor)
        
        painter.drawChord(
            self.scaleContentsRect(), (dir - arc)*16, 2*arc*16)
        # Cria a escala marrom, abaixo da escala azul
        ############################################################
        dir2 = 180 - int(round(self.origin() - self.value()))
        arc2 = 90 + int(round(self.gradient() * 90))
        skyColor2 = Qt.QColor(170, 85, 0)
        #painter.save()
        painter.setBrush(skyColor2)
        
        painter.drawChord(
            self.scaleContentsRect(), (dir2 - arc2 )*16, 2*arc2*16)
        ############################################################
        
        painter.restore()

    # drawScaleContents()
    
# class AttitudeIndicator


class CockpitGrid(Qt.QFrame):
    
    def __init__(self, *args):
        Qt.QFrame.__init__(self, *args)

        self.setPalette(
            self.__colorTheme(Qt.QColor(Qt.Qt.darkGray).dark(150)))
        
        layout = Qt.QGridLayout(self)
       
        layout.addWidget(self.__createDial(),0,1)
        
        #self.__speed_offset = 0.8
        self.__angle_offset = 0.05
        #self.__gradient_offset = 0.005
        
            
    # __init__()
    
    def __colorTheme(self, base):
        background = base.dark(150)
        foreground = base.dark(200)
        
        mid = base.dark(110)
        dark = base.dark(170)
        light = base.light(170)
        text = foreground.light(800)

        palette = Qt.QPalette()
        for colorGroup in colorGroupList:
            # Cor do Corpo do Widget
            palette.setColor(colorGroup, Qt.QPalette.Base, dark)
            #palette.setColor(colorGroup, Qt.QPalette.Background, background)
            # Deixa a borda de uma cor mais escura
            palette.setColor(colorGroup, Qt.QPalette.Mid, mid)
            # Deixa Cor uniforme das bordas do widget
            palette.setColor(colorGroup, Qt.QPalette.Light, light)
            #palette.setColor(colorGroup, Qt.QPalette.Dark, dark)
            # Cor dos indicadores
            palette.setColor(colorGroup, Qt.QPalette.Text, text)
            #palette.setColor(colorGroup, Qt.QPalette.Foreground, foreground)
        
        return palette

    # __colorTheme()

    def __createDial(self):
        dial = None
        self.__ai = AttitudeIndicator(self)
        gradientTimer = Qt.QTimer(self.__ai)
        """
        gradientTimer.connect(gradientTimer,
                              Qt.SIGNAL('timeout()'),
                                    self.changeGradient)
        """
        gradientTimer.start(100)
        angleTimer = Qt.QTimer(self.__ai)
        angleTimer.connect(
        angleTimer, Qt.SIGNAL('timeout()'), self.changeAngle)
        angleTimer.start(5)
        dial = self.__ai
        dial.setToolTip("Horizonte Artificial")
        
        if dial:
            #dial.setReadOnly(True)
            dial.scaleDraw().setPenWidth(3)
            dial.setLineWidth(3)
            #dial.setFrameShadow(Qwt.QwtDial.Sunken)

        return dial
    
    
    # __createDial()
    """
    def changeSpeed(self):
        speed = self.__speedo.value()
        if ((speed < 40.0 and self.__speed_offset < 0.0)
            or (speed > 200.0 and self.__speed_offset > 0.0)):
            self.__speed_offset = -self.__speed_offset
        r = random.randrange(12)
        if r < 6:
            self.__speedo.setValue(speed + r*self.__speed_offset)

    # changeSpeed()
    """
    
    def changeAngle(self):
        angle = self.__ai.angle()
        if angle > 180.0:
            angle -= 360.0

        if ((angle < -35.0 and self.__angle_offset < 0.0 )
            or (angle > 35.0 and self.__angle_offset > 0.0)):
            self.__angle_offset = -self.__angle_offset
            
        self.__ai.setAngle(angle + self.__angle_offset)

    # changeAngle()
    # NÃO É URILIZADO
    def changeGradient(self):
        gradient = self.__ai.gradient()

        if ((gradient < -0.05 and self.__gradient_offset < 0.0 )
            or (gradient > 0.05 and self.__gradient_offset > 0.0)):
            self.__gradient_offset = -self.__gradient_offset

        self.__ai.setGradient(gradient + self.__gradient_offset)

    # changeGradient()

# class CockpitGrid


def make():
    demo = Qt.QTabWidget()
    #demo.addTab(CompassGrid(), "Compass")
    demo.addTab(CockpitGrid(), "Horizonte Artificial")
    """
    demo.setStyleSheet("background: transparent")
    demo.setAttribute(Qt.Qt.WA_TranslucentBackground)
    demo.setWindowFlags(Qt.Qt.FramelessWindowHint)
    """
    demo.show()
    return demo

# make()


def main(args):
    app = Qt.QApplication(args)
    demo = make()
    
    sys.exit(app.exec_())

# main()


# Admire!
if __name__ == '__main__':
    if 'settracemask' in sys.argv:
        # for debugging, requires: python configure.py --trace ...
        import sip
        sip.settracemask(0x3f)

    main(sys.argv)
    
    
    
# Local Variables: ***
# mode: python ***
# End: ***