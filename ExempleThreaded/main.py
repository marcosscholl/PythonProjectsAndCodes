#!/usr/bin/env python
import sys

from PyQt4.QtGui import QApplication
from simulator import MainForm

def main():
  app = QApplication(sys.argv)
  form = MainForm()
  form.show()
  app.exec_()

if __name__ == "__main__":
  main()