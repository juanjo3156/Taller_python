# Para crear una tupla se puede usar la siguiente sintaxis
numeros = (1, 2, 3, 4, 5)

print(numeros)
print(type(numeros))

# Se recomienda definir tuplas de la siguiente forma
frutas = tuple(["Manzana", "Uva", "Pera", "Platano"])


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