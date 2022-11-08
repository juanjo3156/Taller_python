palabra = " días"
#para concatenar un dato numerico 
#hay que convertirlo a str
numero = 10
# print("tengo "+str(numero)+" años")

#las comas dejan un espaciado automatico al momento de
#concatenar 
#si concatenamos dentro de una
#variable obtendremos una tupla
concoma = "hola",numero
print("======con coma=====")
print(concoma)

#En esta forma de concatenación no importa el tipo de dato
#La sintaxis consiste en un {0} (entre llaves) en el sitio
#en el que se concatenara el dato
print("======con format======")
palabra2 = "Aldo"
print("me cae muy mal mi compa el {0}".format(palabra2))

#Es la forma mas practica debido a que 
#es facil de entender y con hay necesidad 
#de convertir los datos
print("=====con f=====")
palabra3 = 512

print(f"Quiero una {palabra3}")