# Las tuplas se pueden definir de la siguiente forma
tupla = tuple()
tupla = (1, 2, 3, "Hola", 1.2)
print(tupla)

tupla2 = 1,2,3,4
print(type(tupla2))

# Agregar datos a una tupla
lista = list(tupla)
print(lista)
lista.append("Adios")
tupla = tuple(lista)
print(tupla)