#Numeros en Python
entero_a = 5
entero_b = 10
decimal_a = 3.0

#para imprimir - print o print()
print entero_a,entero_b,decimal_a
#print entero_b
#print decimal_a

suma_a = entero_a + entero_b

#Numero to String - str()
cadena_suma = str(suma_a)
print ("Suma : " + cadena_suma)

operacion_larga = ((entero_a * entero_b)/decimal_a)+1000
cadena_opl = str(operacion_larga)
print "Rpta OPL = " + cadena_opl

#type - metodo para obtener el tipo de variable
tipo_variable = str(type(operacion_larga))
print "OPL es : " + tipo_variable

#Conversiones
print "OPL to 'int' = " + str(int(operacion_larga))
print "10 a float() --> " + str(float(10))
print "10 a long() --> " + str(long(10))

#str - obtiene el valor absoluto
print "Valor absoluto de 10 : " , str(abs(10))
print "Valor absoluto de 10 .0 : " , str(abs(10.0))

#redondear un numero con round()
print "Float a (3) decimales : " , round(operacion_larga,3)
print "Float a (2) decimales : " , round(operacion_larga,2)
print "Float a (1) decimales : " , round(operacion_larga,1)
