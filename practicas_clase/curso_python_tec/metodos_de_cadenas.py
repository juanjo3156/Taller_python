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

