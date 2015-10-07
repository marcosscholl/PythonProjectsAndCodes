# -*- coding: utf-8 -*-
"""
Created on Thu Dec 18 19:08:27 2014

@author: MarcosScholl
"""
import time 
#U:0:0;W:1:1

txt = raw_input('Entre com alguma coisa:\n')

while (txt != "sair"):  
    print txt
    comando = txt.split(";")
    print "Leu: " 
    print comando
    for comando in comando:
        print "Separado: " 
        print comando
        comandos = comando.split(":")
        print "Completo = " 
        print comandos
        for comando in comandos:
            print "Envia para o Arduino "
            print comando
        print "Vai para a proximo comando"
    print len(comando)

    #time.sleep(1)
    txt = raw_input('Entre com alguma coisa:\n')
print "Bye!"

"""
txt = raw_input('Entre com alguma coisa:\n')

while (txt != "sair"):  
    print txt
    comando = txt.split(";")
    print comando
    for comando in comando:
        comandos = comando.split(":")
        print comandos
    print len(comandos)

    time.sleep(1)
    txt = raw_input('Entre com alguma coisa:\n')
print "Bye!"

"""