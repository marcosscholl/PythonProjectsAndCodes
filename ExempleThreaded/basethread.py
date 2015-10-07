from PyQt4 import QtCore

class BaseThread(QtCore.QThread):
  def __init__(self):
    QtCore.QThread.__init__(self)
    self.exiting = False

  def __del__(self):
    self.exiting = True
    self.wait()