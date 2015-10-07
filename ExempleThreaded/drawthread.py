from time import sleep
from PyQt4 import QtCore
from basethread import BaseThread

class DrawThread(BaseThread):
  def __init__(self):
    BaseThread.__init__(self)

  def run(self):
    while not self.exiting:
      self.emit( QtCore.SIGNAL('DrawCanvas()') )
      sleep(0.05)