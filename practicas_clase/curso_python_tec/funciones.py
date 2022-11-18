# Función simple para saludar
def saludar(nombre):
    print(f"Hola, {nombre}")

#saludar("Juanito Alcachofa")


# Ejemplo función con parámetros
def usuario(nombre, apellido, edad=0):
    print(f"Hola, soy {nombre} {apellido}, y tengo {edad} años.")

usuario(nombre="Rafael", apellido="Vera", edad=22)
usuario(nombre="Rafael", apellido="Vera")
#usuario(edad=22, apellido="Vera", nombre="Rafael")