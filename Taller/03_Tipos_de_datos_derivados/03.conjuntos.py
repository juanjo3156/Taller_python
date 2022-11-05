# Para crear un conjunto se puede usar la siguiente sintaxis
conjunto = {1, 2, 3}
print(conjunto)
print(type(conjunto))

# Si se va a crear un conjunto vacio se debe hacer explicitamente con la funcion 'set()'
conjunto_vacio = set()

# Tambien se puede inicializar con la funcion 'set()'
nombres = set(["Juan", "Angel", "Rafael"])


"""
Propiedades de los conjuntos:
    * Se pueden modificar (agregar y eliminar elementos)
    * No acepta valores repetidos
    * Se ordenan en automatico
"""
numeros = set()

numeros.add(2)
numeros.add(5)
numeros.add(3)
print(numeros)

numeros.add(1)
numeros.remove(5)
numeros.add(4)
numeros.add(4)
numeros.add(4)
print(numeros)