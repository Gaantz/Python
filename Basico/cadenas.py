#Cadenas en Python

cadena_a = "Simple String"
print cadena_a

#Imprimir cadenas largas
cadena_larga =  """Its lorem ipsum Its lorem ipsum Its lorem ipsum
Its lorem ipsum Its lorem ipsum Its lorem ipsum
Its lorem ipsum Its lorem ipsum Its lorem ipsum
Its lorem ipsum Its lorem ipsum Its lorem ipsum
Its lorem ipsum Its lorem ipsum Its lorem ipsum"""
print cadena_larga

#Concatenar cadenas
message = 'Esto es ' + 'un mensaje'
print message

#Repetir cadenas
cadena_repetir = 'Repeat\n'
print cadena_repetir*5

#Concatenar automaticamente 'Cadenas'
#Solo funciona con literales
concatenada = 'Cadena' 'Concatenada'
print concatenada
print 'Concatenando..'.strip()+'!!! \n'

#Cadenas indexadas
palabra = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
print palabra
print palabra[0]
print palabra[1]
print palabra[2]
print palabra[3]
print palabra[4]

#Primeros y ultimos
print palabra[:5]
print palabra[5:]
print palabra[1:3]
