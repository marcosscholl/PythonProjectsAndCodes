from PyQt4 import QtGui, QtCore

from simulator_ui import Ui_Ui_main
from particlecanvas import ParticleCanvas

from drawthread import DrawThread
from stepthread import StepThread

class MainForm(QtGui.QMainWindow):
  def __init__(self, parent=None):
    QtGui.QWidget.__init__(self,parent)
    self.ui = Ui_Ui_main()
    self.ui.setupUi(self)
    self.connect(self.ui.btnSetup, QtCore.SIGNAL("clicked()"), self.on_setup_clicked)
    self.connect(self.ui.btnRun, QtCore.SIGNAL("clicked()"), self.on_run_clicked)
    self.c = ParticleCanvas(self.ui.frame)
    self.pp = DrawThread()
    self.mm = StepThread()
    self.connect( self.pp, QtCore.SIGNAL('DrawCanvas()'), self.c.redraw)
    self.connect( self.mm, QtCore.SIGNAL('TakeStep()'), self.c.move)

  def on_setup_clicked(self):
    self.c.reinitialize(int(self.ui.txtNPart.text()))
    self.mm.exiting = True
    self.pp.start()

  def on_run_clicked(self):
    self.mm.simulate(int(self.ui.txtNSteps.text()))