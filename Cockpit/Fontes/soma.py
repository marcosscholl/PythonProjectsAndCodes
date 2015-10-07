dic = {'nome': 'Shirley Manson', 'banda': 'Garbage'}
print dic['nome']
print dic['banda']

dic['album'] = 'Version 2.0'
print dic['album']

progs = {'Yes': ['Close To The Edge', 'Fragile'],
		'Genesis': ['Foxtrot', 'The Nursery Crime'],
		'ELP': ['Brain Salad Surgery']}
print '\n'
print progs.items()

print '\n'
print progs.keys()

print '\n'
print progs.values()
print '\n'
# items() retorna uma lista de
# tuplas com a chave e o valor
for prog, albuns in progs.items():
	print prog, '=>', albuns



"""
t = ([1,2], 3)
t[0].append(5)
print t
print t[0]
t[0].pop()
print t

print t.__sizeof__()

print t.count([1,2])

print t.__rmul__(2)
t = t.__rmul__(2)
print t
print t[3]
"""

"""
lista = ['A', 'B', 'C']
while lista:
 	print("Saiu ", lista.pop(0), " Tamanho lista: ", len(lista))

lista.append('D')
lista.append('E')
lista.append('F')
while lista:
	print('Saiu ', lista.pop(), 'Tamanho Lista', len(lista))
"""

