# Para crear un conjunto se puede usar la siguiente sintaxis
conjunto = {1, 2, 3}
print(conjunto)
print(type(conjunto))

#Se pueden agregar distintos tipos de elementos
conjunto_2 = {True, 3.14, None, False, "Hola mundo", (1, 2)}

#No puede tener otros objetos mutables
# s = {[1, 2]}


# Si se va a crear un conjunto vacio se debe hacer explicitamente con la funcion 'set()'
conjunto_vacio = set()


# Tambien se puede inicializar con la funcion 'set()'
nombres = set(["Juan", "Angel", "Rafael"])
print(nombres)


"""
Propiedades de los cojuntos:
    * Se pueden modificar (agregar y eliminar elementos)
    * mbres acepta valores repetidos
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