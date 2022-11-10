# # Las listas se pueden definir de la siguiente forma
# lista = [1, 2, 3, 4, "Cinco", 6.0]
# lista_1 = list()

# # Agregando datos a una lista
# lista_1.append(10)
# lista_1.append("Texto")
# lista_1.append('a')
# print(lista)
# print(lista_1)

# # Acceder a los datos dentro de una lista
# lista_1.append([1, 2, 3])
# print(lista_1)
# print(lista_1[3])
# lista_1[3].append(4)
# print(lista_1[3])

# # Obtener el indice de un dato en una lista
# lista_3 = [1, 1, 1, 2, 2, 3, 1]
# print(lista_3)
# print(lista_3.index(2))

# # Ordenando una lista
# lista_4 = [73, 14, 36, 153, 32]
# lista_4.sort()
# print(lista_4)

# nombres = ["Juan", "Pedro", "Angel", "Bruno", "Roberto"]
# nombres.sort()
# print(nombres)


lista = [1,2,3,4,5]
print(len(lista))#con len podemos ver la 
#catidad de datos dentro de nuestra lista


lista.append(6)#Podemos agregar un dato 
# al final de la lista
print(lista)

agregado = [7,8,9]
lista.extend(agregado)#extend agrega datos a una lista 
#a partir de otra lista previamente creada
#y los añade de golpe
print(lista)

lista.remove(7)#permite remover un dato de una lista 
#si es que lo conocemos
print(lista)

lista.pop()#remueve el ultimo dato de la lista
print(lista)

lista2 = ["hola","hola",23,21,56,23,23,"adios"]
#count nos permite contabilizaR la cantidad de veces que 
#se repite un dato conocido
print(lista2.count("america"))

lista.reverse()
print(lista)

animales = ["Vaca","Conejo","Perro","Delfin"]
animales.sort()
print(animales)
# lista_tipos = [1,3.12,False,"texto"]
# print(lista_tipos)

# Dada una la siguiente lista
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(lista)

# Se puede recorrer a la inversa
print(lista[::-1])

# También funciona en Strings
texto = "Hola, buenas tardes"
print(texto[::-1])

# Se puede eliminar elementos de la siguiente forma
# del lista[2]
# print(lista)

# También cambiar el valor de los elementos
# lista[4] = 5
# print(lista)

# diccionario = {
#     1: "Uno",
#     2: "Dos",
#     3: "Tres"
# }
# print(diccionario)

# diccionario[4] = "Cuatro"
# print(diccionario)