'''
Las siguientes lineas son un copy/paste del ejemplo DialDemo.py de las librerias pyqwt.
Lo que hice fue copiar las clases AttitudeIndicator, AttitudeindIndicatorNeedle y la funcion enumList.
Con pequenias modificaciones.
'''

import math
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
        #setclipregion asigna una area de dibujado, lo que este fuera de esta area no se dibuja , si es un circulo, todo lo que este
        #fuera del circulo no se dibujara
        painter.setClipRegion(Qt.QRegion(Qt.QPolygon(pa)))
        Qwt.QwtDial.drawScale(
            self, painter, center, radius, origin, minArc, maxArc)
        painter.restore()
        
    # drawScale()
    
    def drawScaleContents(self, painter, center, radius):
        #para entenderlo mejor chord de un circle - http://www.mathwarehouse.com/geometry/circle/chord-of-circle.php
        #que hace drawchordhttp://doc.trolltech.com/4.6/qpainter.html#drawChord
        dir = 360 - int(round(self.origin() - self.value()))
        arc = 90 + int(round(self.gradient() * 90))
        skyColor = Qt.QColor(38, 151, 221)
        painter.save()
        painter.setBrush(skyColor)
        #lo siguiente a sido modificado para asemejar el widget a un indicador de altitud real
        #al cambiar de qrect a coordenas x,y,width,height puedo agregarle es espacio perdido por las lineas de medida de los angulos
        rectQt = self.scaleContentsRect()
        rect = rectQt.getRect()
        painter.drawChord(
            rect[0]-10, rect[1]-10, rect[2]+20, rect[3]+20, (dir - arc)*16, 2*arc*16)
        painter.restore()

    # drawScaleContents()

# class AttitudeIndicator

class AttitudeIndicatorNeedle(Qwt.QwtDialNeedle):

    def __init__(self, color):
        Qwt.QwtDialNeedle.__init__(self)
        palette = Qt.QPalette()
        for colourGroup in colorGroupList:
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
