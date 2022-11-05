# Para crear una lista podemos usar la siguiente sintaxis

lista = [1,2,3,4,5]
colores = ["azul","rojo","verde","amarillo"]

#print(colores)
lista_numeros = list((1,2,3,4,5,6,7))
print(type(lista_numeros))

# Se recomienda definir las listas de la siguiente forma
lista = list()


# Definir listas por rangos
lista_rango = list(range(1,11))
# llega hasta el numero que va antes del segundo parametro
print(lista_rango)

# Obtener cantidad de datos dentro de una lista
print(len(colores))