""" Salida de datos """

# Para definir una salida de dato se utiliza la funcion 'print()'
print("Hola")

# La funcion print() tambien puede recibir parametros
# Se puede definir como separar los datos que se mandan a imrpimir
print("Hola","mundo", sep=" ") # Por defecto es un caracter vacio

# Se puede definir un caracter al final de la impresion
print("Adios...", end="") # Por defecto es un salto de linea

# Tambien se puede definir vacio y solo imprime el salto de linea
print()


""" Entrada de datos """

# Para definir una entrada de datos se utiliza la funcion 'input()'
entrada = input("Escribe algo: ")

# Este dato se puede mostrar en pantalla
print(entrada)

# El tipo de dato del input es 'str'
print(type(entrada))

# Se puede cambiar el tipo de dato que se recibe
numero_in = int(input("Ingresa un numero: "))
print(numero_in)
print(type(numero_in))

# Nota: Lo que se ingresa debe corresponder al tipo de dato
# Si se ingresa algo que no corresponde dará error
numero_in = int(input("Solo acepto numeros enteros: "))