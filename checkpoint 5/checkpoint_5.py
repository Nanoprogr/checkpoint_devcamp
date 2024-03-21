#crea un bucle for in python
for x in range(1, 11):
    print(x)

#funcion suma con tres argumentos
def suma(valor1, valor2, valor3):
    sum = valor1 + valor2 + valor3
    print(sum)
suma(1, 2, 3)

#funcion lambda con 3 argumentos
suma = lambda valor4, valor5 , valor6 : valor4 + valor5 + valor6
print(suma(1, 2, 3))

#buscar nombre en lista
nombre = 'Enrique'
lista_nombre = ['Jessica', 'Paul', 'George', 'Henry', 'Adán']
if nombre in lista_nombre:
    print(f'{nombre} está en la lista')
else:
    print(f'{nombre} no está en la lista')