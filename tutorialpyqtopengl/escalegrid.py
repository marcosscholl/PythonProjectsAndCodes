"""
This implements the OpenGL widget
"""

from PyQt4 import Qt, QtGui, QtCore
import PyQt4.Qwt5 as Qwt

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
        
"""
class GlWidget (QGLWidget):
    #A simple OpenGL pane
    
    def __init__ (self, parent=None):
        #Constructor
        super (GlWidget, self).__init__(parent)
        
    def paintGL(self):
        #A Simple drawing callback for drawing one triangle
        glClear (GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT);
        glBegin (GL_TRIANGLES);
        glVertex3f (0, 0, 0);
        glVertex3f (0, 1, 0);
        glVertex3f (1, 0, 0);
        glEnd ();

     
    def resizeGL (self, width, height):
        #A simple resize callback.
        side = min(width,height)
        glViewport((width - side) / 2, (height - side) / 2, side, side);
"""

class CriaEscaleGrid(Qt.QFrame):
    
         
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
        self.Thermo.setGeometry(QtCore.QRect(300, 10, 725, 70))
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
        
class EscaleGrid(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self)
        self.ui = CriaEscaleGrid()
        self.ui.createEscale(self) 
        self.setGeometry(300, 10, 725, 70)
