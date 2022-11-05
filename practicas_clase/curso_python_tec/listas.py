# Las listas se pueden definir de la siguiente forma
lista = [1, 2, 3, 4, "Cinco", 6.0]
lista_1 = list()

# Agregando datos a una lista
lista_1.append(10)
lista_1.append("Texto")
lista_1.append('a')
print(lista)
print(lista_1)

# Acceder a los datos dentro de una lista
lista_1.append([1, 2, 3])
print(lista_1)
print(lista_1[3])
lista_1[3].append(4)
print(lista_1[3])

# Obtener el indice de un dato en una lista
lista_3 = [1, 1, 1, 2, 2, 3, 1]
print(lista_3)
print(lista_3.index(2))

# Ordenando una lista
lista_4 = [73, 14, 36, 153, 32]
lista_4.sort()
print(lista_4)

nombres = ["Juan", "Pedro", "Angel", "Bruno", "Roberto"]
nombres.sort()
print(nombres)