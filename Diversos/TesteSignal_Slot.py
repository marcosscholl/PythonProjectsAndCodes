# -*- coding: utf-8 -*-
"""
Created on Tue Mar 18 10:47:09 2014

@author: MarcosScholl
"""

class Signal(object):
   def __init__(self):
      self.__slotList = []

   def __call__(self, *args, **kwds):
      for slot in self.__slotList:
         slot(*args, **kwds)

   def addSlot(self, slot):
      if not callable(slot):
         raise ValueError('slots must be callable')
      if not slot in self.__slotList:
         self.__slotList.append(slot)

   def delSlot(self, slot):
      try:
         self.__slotList.remove(slot)
      except ValueError:
         pass

   def isConnected(self, slot):
      return slot in self.__slotList

def connect(signal, slot):
   signal.addSlot(slot)

def disconnect(signal, slot):
   signal.delSlot(slot)
# fim da classe signal
'''
O que fazemos aqui é simplesmente definir um objeto que armazenará uma lista de ações que executará. 
Quando chamarmos um objeto Signal, ele chamará cada uma das ações conectadas a ele. Vamos ao exemplo de uso:
'''


def showChange(obj, oldValue):
   print 'Valor alterado de %s para %s.' % (oldValue, obj.value)

def showObject(obj, oldValue):
   print 'Objeto com valor alterado:', obj

class MyClass(object):
   def __init__(self, value):
      self.__value = value
      # Define um sinal observável.
      self.valueChanged = Signal() # (1)

   def setValue(self, value):
      oldValue = self.__value
      self.__value = value
      # Emite u00m sinal informando o objeto e o valor antigo.
      self.valueChanged(self, oldValue) # (2)

   def getValue(self):
      return self.__value

   value = property(getValue, setValue)

def main():
   myObj = MyClass(3)
   # Conecta sinais aos slots.
   connect(myObj.valueChanged, showChange) # (3)
   connect(myObj.valueChanged, showObject) # Simples, não?

   try:
      while True:
         value = raw_input('Novo valor: ')
         myObj.value = value
   except KeyboardInterrupt:
      pass

if __name__ == '__main__':
        main()   
   
'''
Este programa irá ficar perguntando por novos valores, e os setará no objeto criado, até receber uma interrupção do teclado (em geral, Ctrl+C). 

A parte interessante é que existem duas funções monitorando mudanças no valor do atributo value.

Em (1) simplesmente definimos um sinal. 

Em (2) nós o emitimos, quando a propriedade value for alterada. 
A classe Signal fica responsável por chamar todos os slots que observam o sinal. 
Note como fica simples trasmitir informações para nossos observadores. 

Em (3), conectamos os observadores (slots) ao sinal observado.
Uma outra facilidade provida pela classe é poder verificar se um slot está conectado a um determinado sinal, ou em algum ponto desconectar a ação do sinal.
Lendo sobre o assunto, você poderá encontrar vários termos para os Slots, como Observers ou Observadores e Listeners ou Ouvintes.
'''
   
   