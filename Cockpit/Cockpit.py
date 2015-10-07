# -*- coding: utf-8 -*-
"""
Created on Tue Jan 14 18:49:43 2014

@author: MarcosScholl
"""
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
    

##############################################################################################################
##############################################################################################################

class EscaleGrid(Qt.QFrame):

    def createEscale(self, Form):
        Form.setObjectName(_fromUtf8("Form"))
        Form.setWindowModality(QtCore.Qt.ApplicationModal)
        Form.resize(721, 65)
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
        self.Thermo = Qwt.QwtThermo(Form)
        self.Thermo.setGeometry(QtCore.QRect(0, 0, 711, 61))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.Thermo.setFont(font)
        self.Thermo.setAutoFillBackground(False)
        self.Thermo.setStyleSheet(_fromUtf8("color: rgb(0, 0, 0);\n"
""))
        self.Thermo.setInputMethodHints(QtCore.Qt.ImhNone)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.Thermo.setAlarmBrush(brush)
        self.Thermo.setAlarmColor(QtGui.QColor(255, 0, 0))
        self.Thermo.setAlarmEnabled(True)
        self.Thermo.setAlarmLevel(80.0)
        self.Thermo.setScalePosition(Qwt.QwtThermo.TopScale)
        self.Thermo.setBorderWidth(3)
        brush = QtGui.QBrush(QtGui.QColor(0, 85, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        self.Thermo.setFillBrush(brush)
        self.Thermo.setMaxValue(100.0)
        self.Thermo.setPipeWidth(20)
        self.Thermo.setProperty("value", 98.0)
        self.Thermo.setObjectName(_fromUtf8("Thermo"))
        
        return self

class CriaEscalaProfundidade(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = EscaleGrid()
        self.ui.createEscale(self)        

##############################################################################################################
##############################################################################################################

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
    
    
  
############################################################################################################# 
#############################################################################################################  
    
class AttitudeIndicatorNeedle(Qwt.QwtDialNeedle):

    def __init__(self, color):
        Qwt.QwtDialNeedle.__init__(self)
        palette = Qt.QPalette()
        for colourGroup in colorGroupList:
            ## Cor dos Indicadores QtGui.QColor(255, 0, 0)
            palette.setColor(colourGroup, Qt.QPalette.Text, QtGui.QColor(255, 255, 255))
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
            palette.setColor(colorGroup, Qt.QPalette.Background, background)
            # Deixa a borda de uma cor mais escura
            palette.setColor(colorGroup, Qt.QPalette.Mid, mid)
            # Deixa Cor uniforme das bordas do widget
            palette.setColor(colorGroup, Qt.QPalette.Light, light)
            #palette.setColor(colorGroup, Qt.QPalette.Dark, dark)
            # Cor dos indicadores
            palette.setColor(colorGroup, Qt.QPalette.Text, text)
            palette.setColor(colorGroup, Qt.QPalette.Foreground, foreground)
        
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

    
    def changeAngle(self):
        angle = self.__ai.angle()
        if angle > 180.0:
            angle -= 360.0

        if ((angle < -35.0 and self.__angle_offset < 0.0 )
            or (angle > 35.0 and self.__angle_offset > 0.0)):
            self.__angle_offset = -self.__angle_offset
         
        self.__ai.setAngle(angle + self.__angle_offset)
        
##############################################################################################################       
##############################################################################################################
       
import IconsHealth_rc       
               
class Ui_Form(Qt.QFrame):
 
        
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
        self.groupBoxInformacoes.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.groupBoxInformacoes.setTitle(_fromUtf8("Informações Internas"))
        self.groupBoxInformacoes.setObjectName(_fromUtf8("groupBoxInformacoes"))
        self.frameBussola = QtGui.QFrame(self.groupBoxInformacoes)
        self.frameBussola.setGeometry(QtCore.QRect(10, 170, 61, 71))
        self.frameBussola.setToolTip(_fromUtf8("Status GPS"))
        self.frameBussola.setStyleSheet(_fromUtf8("image: url(:/Icons/posicao.png);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.frameBussola.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameBussola.setFrameShadow(QtGui.QFrame.Raised)
        self.frameBussola.setObjectName(_fromUtf8("frameBussola"))
        self.lblTemp = QtGui.QLabel(self.groupBoxInformacoes)
        self.lblTemp.setGeometry(QtCore.QRect(10, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblTemp.setFont(font)
        self.lblTemp.setAutoFillBackground(False)
        self.lblTemp.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
""))
        self.lblTemp.setObjectName(_fromUtf8("lblTemp"))
        self.lblStatus = QtGui.QLabel(self.groupBoxInformacoes)
        self.lblStatus.setGeometry(QtCore.QRect(10, 100, 91, 20))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblStatus.setFont(font)
        self.lblStatus.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
""))
        self.lblStatus.setObjectName(_fromUtf8("lblStatus"))
        self.lblStatusValue = QtGui.QLabel(self.groupBoxInformacoes)
        self.lblStatusValue.setGeometry(QtCore.QRect(70, 120, 161, 41))
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
        self.frameCamera.setToolTip(_fromUtf8("Status Câmera"))
        self.frameCamera.setStyleSheet(_fromUtf8("image: url(:/Icons/camera1.png);\n"
"background-color: rgba(255, 255, 255, 0);\n"
""))
        self.frameCamera.setFrameShape(QtGui.QFrame.StyledPanel)
        self.frameCamera.setFrameShadow(QtGui.QFrame.Raised)
        self.frameCamera.setObjectName(_fromUtf8("frameCamera"))
        self.frameConexao = QtGui.QFrame(self.groupBoxInformacoes)
        self.frameConexao.setGeometry(QtCore.QRect(190, 170, 61, 71))
        self.frameConexao.setToolTip(_fromUtf8("Status Comunicação"))
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
        self.lblTemp_Value = QtGui.QLabel(self.groupBoxInformacoes)
        self.lblTemp_Value.setGeometry(QtCore.QRect(70, 50, 171, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.lblTemp_Value.setFont(font)
        self.lblTemp_Value.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.lblTemp_Value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTemp_Value.setObjectName(_fromUtf8("lblTemp_Value"))
        self.groupBox = QtGui.QGroupBox(Form)
        self.groupBox.setGeometry(QtCore.QRect(5, 0, 261, 191))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);"))
        self.groupBox.setTitle(_fromUtf8("Informações Externas"))
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.lblPressao_Value = QtGui.QLabel(self.groupBox)
        self.lblPressao_Value.setGeometry(QtCore.QRect(50, 135, 191, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.lblPressao_Value.setFont(font)
        self.lblPressao_Value.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.lblPressao_Value.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblPressao_Value.setObjectName(_fromUtf8("lblPressao_Value"))
        self.lblPressao = QtGui.QLabel(self.groupBox)
        self.lblPressao.setGeometry(QtCore.QRect(10, 110, 171, 21))
        font = QtGui.QFont()
        font.setPointSize(20)
        self.lblPressao.setFont(font)
        self.lblPressao.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
""))
        self.lblPressao.setObjectName(_fromUtf8("lblPressao"))
        self.lblTemp_Value_2 = QtGui.QLabel(self.groupBox)
        self.lblTemp_Value_2.setGeometry(QtCore.QRect(80, 50, 161, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Arial"))
        font.setPointSize(35)
        font.setBold(True)
        font.setWeight(75)
        self.lblTemp_Value_2.setFont(font)
        self.lblTemp_Value_2.setStyleSheet(_fromUtf8("color: rgb(255, 255, 255);\n"
"background-color: rgba(255, 255, 255, 0);"))
        self.lblTemp_Value_2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.lblTemp_Value_2.setObjectName(_fromUtf8("lblTemp_Value_2"))
        self.lblTemp_2 = QtGui.QLabel(self.groupBox)
        self.lblTemp_2.setGeometry(QtCore.QRect(10, 20, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.lblTemp_2.setFont(font)
        self.lblTemp_2.setAutoFillBackground(False)
        self.lblTemp_2.setStyleSheet(_fromUtf8("background-color: rgba(255, 255, 255, 0);\n"
"color: rgb(255, 255, 255);\n"
""))
        self.lblTemp_2.setObjectName(_fromUtf8("lblTemp_2"))

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(_translate("Form", "Form", None))
        self.lblTemp.setText(_translate("Form", "Temperatura", None))
        self.lblStatus.setText(_translate("Form", "Status", None))
        self.lblStatusValue.setText(_translate("Form", "OK", None))
        self.lblTemp_Value.setText(_translate("Form", "35 ºC", None))
        self.lblPressao_Value.setText(_translate("Form", "10 m", None))
        self.lblPressao.setText(_translate("Form", "Profundidade", None))
        self.lblTemp_Value_2.setText(_translate("Form", "16 ºC", None))
        self.lblTemp_2.setText(_translate("Form", "Temperatura", None))
        
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
        


class criaHealth(QtGui.QWidget):
    def __init__(self):
        QtGui.QWidget.__init__(self)
        self.ui = Ui_Form()
        self.ui.setupUi(self)       
        
        
        
##############################################################################################################       
##############################################################################################################



if __name__ == '__main__':
    import sys
    
    # BUSSOLA
    app = QtGui.QApplication(sys.argv)
    bussola = CompassGrid()
    
    #  CustomizeWindowHint
    bussola.setWindowFlags(Qt.Qt.FramelessWindowHint)
    
    bussola.setAttribute(Qt.Qt.WA_TranslucentBackground, True)
    bussola.setAttribute(Qt.Qt.WA_NoSystemBackground)
    bussola.setAutoFillBackground(False)
    #bussola.setWindowOpacity(1)  
    bussola.setGeometry(1050, 100, 300, 300)  

    bussola.show()
    #sys.exit(app.exec_()) 
    
    
    ########################################
    # ESCALA
    #app2 = QtGui.QApplication(sys.argv)
    #escala = EscaleGrid()
    escala = CriaEscalaProfundidade()
    
    #escala.setGeometry(QtCore.QRect(0, 0, 711, 61))
    
    escala.setWindowFlags(Qt.Qt.FramelessWindowHint)
        
    escala.setAttribute(Qt.Qt.WA_TranslucentBackground, True)
    escala.setAttribute(Qt.Qt.WA_NoSystemBackground)
    escala.setAutoFillBackground(False)
    #escala.setWindowOpacity(1)
    
    escala.setGeometry(300, 10, 725, 70)
    

    escala.show()
    ##sys.exit(app2.exec_()) 
    
    
    ########################################
    ##  HORIZONTE
    # app3 = QtGui.QApplication(sys.argv)
    horizonte = CockpitGrid()
    
    # Remove Borda Janela
    horizonte.setWindowFlags(Qt.Qt.FramelessWindowHint)
    horizonte.setAttribute(Qt.Qt.WA_TranslucentBackground, True)
    horizonte.setAttribute(Qt.Qt.WA_NoSystemBackground)
    horizonte.setAutoFillBackground(False)
    #horizonte.setWindowOpacity(1)

    horizonte.setGeometry(1050, 400, 300, 300)
    

    horizonte.show()
    
    
    ########################################
    
    # CAMERA
    win = Qt.QWidget()  
    win.setAttribute(Qt.Qt.WA_TranslucentBackground, True)
    win.setAttribute(Qt.Qt.WA_OpaquePaintEvent, False)
    win.setAutoFillBackground(True)
    #win.setStyleSheet("background: transparent")
    win.setWindowFlags(Qt.Qt.FramelessWindowHint)

    # widget sem parent significa que é top-level, ou seja, uma janela
    ##win.setGeometry(200, 200, 0, 0)
    # parametros: x, y, largura, altura
    win.setGeometry(300, 100, 750, 600)
    #win.show()                         
    # o primeiro widget sem parent a ser mostrado torna-se janela principal
    
    
    #######################################
    ##  Health
    
    health = criaHealth()
    
    
    health.setWindowFlags(Qt.Qt.FramelessWindowHint)
    """
    health.setAttribute(Qt.Qt.WA_TranslucentBackground, True)
    health.setAttribute(Qt.Qt.WA_NoSystemBackground)
    health.setAutoFillBackground(False)
    """
    health.setGeometry(10, 100, 270, 445)
    health.show()
    
    #######################################

    
    sys.exit(app.exec_())
    