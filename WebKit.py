# -*- coding: utf-8 -*-
"""
Created on Thu Oct 06 14:49:05 2015

@author: Marcos Vinicius Scholl
@page: 'www.marcosscholl.github.io
"""

import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtWebKit import *
 

 
url = ""
 
class MeuNavegadorFoda(QtGui.QMainWindow):
 
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.createBroswer()
        
 
    def createBroswer(self):
  
        self.centralwidget = QtGui.QWidget(self)
 
        self.line = QtGui.QLineEdit(self)
        self.line.setMinimumSize(1150,30)
        self.line.setStyleSheet("font-size:15px;")
        
        self.enter = QtGui.QPushButton(self)
        self.enter.resize(0,0)
        self.enter.clicked.connect(self.Enter)
        self.enter.setShortcut("Return")
        
        self.reload = QtGui.QPushButton("R",self)
        self.reload.setMinimumSize(35,30)
        self.reload.setShortcut("F5")
        self.reload.setStyleSheet("font-size:23px;")
        self.reload.clicked.connect(self.Reload)
 
        self.back = QtGui.QPushButton("B",self)
        self.back.setMinimumSize(35,30)
        self.back.setStyleSheet("font-size:23px;")
        self.back.clicked.connect(self.Back)
 
        self.forw = QtGui.QPushButton("F",self)
        self.forw.setMinimumSize(35,30)
        self.forw.setStyleSheet("font-size:23px;")
        self.forw.clicked.connect(self.Forward)
        
        self.exit = QtGui.QPushButton("X",self)
        self.exit.setMinimumSize(35,30)
        self.exit.setStyleSheet("font-size:23px;")
        self.exit.clicked.connect(self.Exit)
 
 
        self.web = QWebView()
        self.web.setMinimumSize(1300,650)
        self.web.urlChanged.connect(self.UrlChanged)

 
        grid = QtGui.QGridLayout()
 
        grid.addWidget(self.back,0,0, 1, 1)        
        grid.addWidget(self.forw,0,1, 1, 1)
        grid.addWidget(self.reload,0,2, 1, 1)
        grid.addWidget(self.line,0,3, 1, 1)
        grid.addWidget(self.exit,0,4, 1, 1)
  
        grid.addWidget(self.web, 2, 0, 1, 6)
 
        self.centralwidget.setLayout(grid) 
        self.setGeometry(50,50,1300,650)
        self.setWindowTitle("Navegador 'www.marcosscholl.github.io'")
        self.setCentralWidget(self.centralwidget)

        

    def Enter(self):
        global url
         
        url = self.line.text()
        if url == "xxx":
            self.web.load(QtCore.QUrl("http://ifolderlinks.ru/404/"))
            return
 
        http = "http://"
        www = "www."
         
        if www in url and http not in url:
            url = http + url
             
        elif "." not in url:
            url = "http://www.google.com/search?q="+url
             
        elif http in url and www not in url:
            url = url[:7] + www + url[7:]
 
        elif http and www not in url:
            url = http + www + url 
 
        self.web.load(QtCore.QUrl(url))
        
   
 
    def Back(self):
        self.web.back()      
 
         
    def Forward(self):
        self.web.forward()
 
    def Reload(self):
        self.web.reload()
 
    def UrlChanged(self):
        self.line.setText(self.web.url().toString())
 
        
    def Exit(self):
        self.close()
        
    def OpenMyPage(self):
        self.web.load(QtCore.QUrl('http://marcosscholl.github.io/'))
 
 
if __name__ == "__main__":
    app = QtGui.QApplication(sys.argv)
    melhorQueChrome = MeuNavegadorFoda()
    melhorQueChrome.show()
    melhorQueChrome.OpenMyPage()
 
    sys.exit(app.exec_())
