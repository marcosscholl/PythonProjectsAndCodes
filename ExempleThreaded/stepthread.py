from time import sleep
from PyQt4 import QtCore
from basethread import BaseThread

class StepThread(BaseThread):
  def __init__(self):
    BaseThread.__init__(self)

  def simulate(self, nsteps):
    self.nsteps = nsteps
    self.exiting = False
    self.start()

  def run(self):
    while not self.exiting and self.nsteps > 0:
      self.emit( QtCore.SIGNAL('TakeStep()') )
      self.nsteps -= 1
      sleep(0.005)