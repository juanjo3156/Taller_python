texto = "El veloz murciélago hindú comía feliz cardillo y kiwi. \
La cigüeña tocaba el saxofón detrás del palenque de paja."
print(texto)

# Contar el número de ocurrencias de una cadena
print(texto.count("el", 20, 80))

# Encontrar la posición donde se da la ocurrencia
#print(texto.find("triste"))
#print(texto.index("triste"))

# Validar si inicia o termina con algún patrón
print(texto.startswith("veloz"))
print(texto.endswith("paja."))

texto2 = "123"

# Validar si la cadena de texto está compuesta por puros números
print(texto.isnumeric())
print(texto2.isnumeric())
print(texto.isdigit())
print(texto2.isdigit())
print(texto.isdecimal())
print(texto2.isdecimal())

texto3 = "cARlOs hErnAnDez"

# Cambia el primer caracter por mayúscula
print(texto3.capitalize())

# Cambia todo el texto a minúsculas
print(texto3.lower())
# Cambia todo el texto a mayúsculas
print(texto3.upper())
# Intercambia mayúsculas por minúsculas y viceversa
print(texto3.swapcase())

texto4 = "____ahak__jhfk____"
# Elimina los caracteres indicados de inicio y fin de la cadena
print(texto4.strip("_"))
# Elimina los caracteres indicados al inicio de la cadena
print(texto4.lstrip("_"))
# Elimina los caracteres indicados al final de la cadena
print(texto4.rstrip("_"))
# Reemplaza los caracteres por otro dado
print(texto4.replace("_", "*"))

texto5 = "hola"

print(texto5.center(10, "."))
print(texto5.ljust(10, "*"))
print(texto5.rjust(10, "_"))

texto6 = "Buenas tardes"
tabla = texto6.maketrans("Bea", "Giz", "s")
print(texto6.translate(tabla))

lista = texto.split("e")
print(lista)

print("a".join(lista))

lista_de_palabras = input().split()
print(lista_de_palabras)