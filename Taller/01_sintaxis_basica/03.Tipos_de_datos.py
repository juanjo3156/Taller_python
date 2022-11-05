#Tipos de datos 
texto = "texto"    # Cadena de caracteres
numero = 10        # Numeros enteros
flotante = 3.6     # Numeros con decimales
booleana = True    # Booleanos
vacio = None       # Nulo

#imprimiendo tipos de datos
print(type(texto))
print(type(numero))
print(type(flotante))
print(type(booleana))
print(type(vacio))

# También se puede "definir" el tipo de dato a una variable
texto : str = "texto"
numero : int = 10
flotante : float = 3.6
booleana : bool = True

# Pero esto no es absoluto
texto : str = 10