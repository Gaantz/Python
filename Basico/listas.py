#Listas en Python
lista_numeros = [1,2,3,4,5,6,7,8,9,10]
lista_cadenas = ['a','b','c','d','e','f','g','h','i','j']
lista_mixta = [1,'a',2,'b',3,'c',4,'d',5,'e']

print lista_numeros
print lista_cadenas
print lista_mixta

#Indices de lista
print lista_numeros[0]
print lista_cadenas[-5]

print lista_mixta[3:-5]
print lista_numeros[0:-9]
print lista_cadenas[0:-9]

#Indices Mayores de 'x:'
print lista_numeros[2:]
print lista_cadenas[5:]
print lista_mixta[7:]

#Indices Menores de ':x'
print lista_numeros[:2]
print lista_cadenas[:5]
print lista_mixta[:7]

#Multiplicando listas
print 2*lista_numeros[:9]

#Reemplazar items de una lista
lista_cadenas[1:3] = ['z','w']
print lista_cadenas

#Borrar items de una lista
lista_cadenas[0:2] =[]
print lista_cadenas

#Crear lista con listas adentro
lista_general = ['-1','-2',lista_numeros,lista_cadenas,lista_mixta]
print lista_general

lista_general[2].append(100)
print lista_general

lista_general[2][0] = -100
print lista_general
