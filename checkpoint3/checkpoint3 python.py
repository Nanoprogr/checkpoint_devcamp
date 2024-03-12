# variables
linea = 'johan'
print('Varible string\n', linea , type(linea))

numero_entero = 5
print('Varible numero entero\n', numero_entero , type(numero_entero))

numero_decimal = 10.9
print('Varible numero decimal\n', numero_decimal , type(numero_decimal))

numero_imaginario = 10 + 9j
print('Varible numero imaginario\n', numero_imaginario , type(numero_imaginario))

lista = [1,3,5,'johan',10.9] 
print('Varible lista\n', lista , type(lista))

boleano = True
print('Varible boolean\n', boleano , type(boleano))

#tomar las primeras 3 letras de mi string
mi_cool_string = 'johan aprende a programar en Python'
mis_letras = mi_cool_string [0:3]
#otra forma de tomar las primeras 3 letras de mi string
mis_letras_2 = mi_cool_string [:3]
print ('Mis tres primeras letras son:\n',mis_letras, mis_letras_2)

#tomar el primer elemto de una lista
mi_cool_list = ['johan', 'aprende', 'programar', 'en', 'Python']
mi_elemento = mi_cool_list [0]
print ('Mi primer elemento es:\n', mi_elemento)

#crear una variable que sume 10 a mi varible numerica
import operator
from re import split
suma_10 = operator.add(10,numero_entero)
print('Variable numero que suma 10 a mi variable original;\n', suma_10, type(suma_10))

#tomar el ultimo elemtno de mi lista
ultimo_elemento = mi_cool_list [-1]
print('Ultimo elemento de la lista\n', ultimo_elemento)

#convertir string en lista
names = 'harry,alex,susie,jared,gail,conner'
lista_de_nombres = names.split(',')
print ('esta es la lista de nombres\n', lista_de_nombres, type(lista_de_nombres))

'''tomar la primera palabra en mi string, ponerla en mayusculas
y agregarla cambiarla por la original modo 1
'''
mi_to_upper_string = mi_cool_string.split()
mi_upper_name = mi_to_upper_string[0].upper()
mi_nueva_linea = mi_upper_name + mi_cool_string[5:]
print ('esta es la nueva linea\n',mi_nueva_linea, type(mi_nueva_linea))

'''tomar la primera palabra en mi string, ponerla en mayusculas
y agregarla cambiarla por la original modo 1
'''
mi_to_upper_string_two = mi_cool_string.split()
mi_word = mi_to_upper_string_two[0]
mi_upper_name_two = mi_to_upper_string_two[0].upper()
mi_nueva_line_two = mi_cool_string.replace(mi_word, mi_upper_name_two)
print ('esta es la otra nueva linea\n',mi_nueva_line_two, type(mi_nueva_line_two))