# -*- coding: utf-8 -*-
"""
Created on Mon Jan 13 10:42:09 2014

@author: MarcosScholl
"""
from PyQt4.QtGui import *
from PyQt4.QtCore import Qt
#from PyQt4 import Qt
import sys
  
def main():
     app = QApplication(sys.argv)       # precisa ser criado antes de mais nada! recebe argumentos da linha de comando
     win = QWidget()  
     win.setAttribute(Qt.WA_TranslucentBackground, True)
     win.setAttribute(Qt.WA_OpaquePaintEvent, False)
     win.setAutoFillBackground(True)
     #win.setStyleSheet("background: transparent")
     win.setWindowFlags(Qt.FramelessWindowHint)


                  # widget sem parent significa que é top-level, ou seja, uma janela
     ##win.setGeometry(200, 200, 0, 0)
     # parametros: x, y, largura, altura
     win.setGeometry(120, 100, 900, 600)
     win.show()                         # o primeiro widget sem parent a ser mostrado torna-se janela principal
     sys.exit(app.exec_())              # exec_() dispara o mainloop, e ao terminar, encerra-se o interpretador
  
if __name__ == '__main__':
    main()