

import sys,  time , serial #,  winsound
import math
from PyQt4 import QtCore, QtGui
from Ui_testanalogdialui import Ui_MainWindow
import PyQt4.Qwt5 as Qwt
import clases
import string
grad2rad = 3.141592/180.0

class testAnalogDial(QtGui.QMainWindow):
    
   
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #para crear los beeps en linux
        #open('/dev/dsp','w').write(''.join(chr(128 * (1 + math.sin(math.pi * 440 * i / 100.0))) for i in xrange(1000)))

        #self.ptoSerial = serial.Serial('/dev/ttyUSB0',  9600,  timeout = 1)
        self.ptoSerial = serial.Serial('COM3',  115200,  timeout = 1)
        self.timer = QtCore.QTimer()       
        self.connect(self.timer, QtCore.SIGNAL("timeout()"), self.timerEvent)

        #se llama a la funcion que dibuja el dial incluida en el archivo clases
        self.ind = clases.AttitudeIndicator(self)
        
        #se modifican las propiedades
        #si es readonly no acepta el mouse ni el keypress
        self.ind.setReadOnly(True)
        self.ind.scaleDraw().setPenWidth(3)
        self.ind.setLineWidth(4)
        self.ind.setFrameShadow(Qwt.QwtDial.Sunken)
        #se dibuja el dial en el widget
        self.ui.vlDial.addWidget(self.ind)
               
        #el gradient lo que hace es indicar el nivel de "cielo" si es uno es que la punta esta hasta arriba
        #si es -1 es que la punta apunta totalmenta hacia tierra
        self.ind.setGradient(0)
        self.ind.setAngle(50)
        self.timer.start(10)
        self.x = 0
        self.y = 0
        self.z = 0
            
    
    def timerEvent(self):
        angX, gradY, freeFall = self.decodeData() 
        self.ind.setAngle(angX)
        self.ind.setGradient(gradY)
        if freeFall == True:
            self.ui.lblImg.setPixmap(QtGui.QPixmap(":/img/imagenes/circle_red.png"))
            #beeps
            #winsound.Beep(1000, 50)
            #winsound.Beep(1000, 50)
            #winsound.Beep(1000, 50)
            #open('/dev/dsp','w').write(''.join(chr(128 * (1 + math.sin(math.pi * 440 * i / 100.0))) for i in xrange(1000)))
            #open('/dev/dsp','w').write(''.join(chr(128 * (1 + math.sin(math.pi * 440 * i / 100.0))) for i in xrange(1000)))
            #open('/dev/dsp','w').write(''.join(chr(128 * (1 + math.sin(math.pi * 440 * i / 100.0))) for i in xrange(1000)))
            
        else:    
            self.ui.lblImg.setPixmap(QtGui.QPixmap(":/img/imagenes/circle_grey.png"))
        
    def decodeData(self):
        data = self.ptoSerial.readline()
        print "Data:", data
        #data = data.split(",")
        #print "data[2]:", data[2]
       
        words = data.split(",")    # Fields split
        print "words:", words
        if len(words) > 2:
            try:
                self.x = float(words[0])
                self.y = float(words[1])
                self.z = float(words[2])
            except:
                print "Invalid line"
        #print "X:", self.x
        #print "Y:", self.y
        #print "Z:", self.z
        #el minimo es 71 y el maximo es 195 . 195-71 = 123. 123 / 180 grados = 1.463  por grado
        #en reposo esta en 143 pero debe de estar en 123, el problema es que esta mal soldado, no estan los pines a 90 grados
        self.x = self.x - 20
        angX = (1.463 * self.x) -180
        
        #par y aproximadamente el minimo es de 65 y el maximo es de 191. 191-65 = 126. va de -1.00 a 1.00.
        #65 *1.587  aprox 103 minimo equivale al  -1.00 (hacia el cielo)
        #191 * 1.587 aprox 303 maximo equivale al 1.00 (hacia la tierra)
        #diferencia entre 303-103 es igual a 200
        #para que la punta cuando suba apunte al cielo
        gradY = ((1.587 * self.y) - 200) / 100

        #el eje z es el detector de freefall si es mayor a 200 entonces esta en caida libre
        if self.z < -160 :
            freeFall = True
        else:
            freeFall = False
        return angX, gradY,  freeFall
        #return float(words[0])*grad2rad, float(words[1])*grad2rad, False



if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    myapp = testAnalogDial()
    #WidgetThread = threading.Thread(target=myapp.thread, ) 
    #WidgetThread.start()
    myapp.show()
    sys.exit(app.exec_())
    
