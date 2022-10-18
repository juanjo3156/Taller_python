#concatenación

#concatenar cadenas 
print("Hola "+"mundo")

mundo = "mundo"
print("Hola "+mundo)

#concatenar numeros con cadenas

#para lograr concatenar cadenas con numeros debemos convertir los numeros a tipo cadena
print("=======concatenación entre numeros y cadenas=========")
print("numero: "+str(10)+" numero: "+str(4))


#con variables
#podemos usar el metodo str() para convertir un dato numerico a tipo cadena
n1 = 5

print("=======concatenado con una variable=======")
print("El numero cinco: "+str(n1))


#el dato sigue siendo entero siempre y cuando no cambiemos el valor de la variable 
print("=======Tipo=========")

print(n1)
print(type(n1))


#concatenacion con format
print("=======concatenación format=======")
strinng = "Juan"
print("Hola mi nombre es {0}".format(strinng))


#Concatenación con f

print("=======concatenación con f (format)=======")
#mucho mas eficiente debido a que no hay necesidad de convertir los datos numericos a strings
#y es mucho mas entendible la sintaxis
edad = 22
nombre = f"Juan José tiene {edad} años de edad"
print(nombre)

#incluso podemos hacer operaciones matematicas dentro del mismo string
resultado = f"la suma da como resltado: {5+5}"
print(resultado)


