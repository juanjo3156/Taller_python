# Las tuplas se pueden definir de la siguiente forma
tupla = tuple()
tupla = (1, 2, 3, "Hola", 1.2)
print(tupla)

# Agregar datos a una tupla
lista = list(tupla)
lista.append("Adios")
tupla = tuple(lista)
print(tupla)