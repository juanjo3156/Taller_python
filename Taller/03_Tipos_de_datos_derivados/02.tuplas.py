# Para crear una tupla se puede usar la siguiente sintaxis
numeros = (1, 2, 3, 4, 5)
print(numeros)
print(type(numeros))

#definiendo tupla por comas
tupla = 1, 2, 3
print(type(tupla))
print(tupla)

# Se puede convertir una lista a tupla con la función tuple()

#convirtiendo
lista = [1, 2, 3]
tupla = tuple(lista)
print(type(tupla))

"""
Nota: Las tuplas por si solas no son modificables,
pero hay trucos para modificarlas.
"""



nombres = tuple(["Juan", "Angel", "Rafael"])
print(nombres)

# Agregar elementos a una tupla
nombres = list(nombres)
nombres.append("Jose")
nombres = tuple(nombres)
print(nombres)

# Eliminar elementos a una tupla
nombres = list(nombres)
nombres.remove("Juan")
nombres = tuple(nombres)
print(nombres)