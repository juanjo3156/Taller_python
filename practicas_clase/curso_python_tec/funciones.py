# # Función simple para saludar
def saludar(nombre):
    print(f"Hola, {nombre}")

#saludar("Juanito Alcachofa")


# Ejemplo función con parámetros
def usuario(nombre, apellido, edad=0):
    print(f"Hola, soy {nombre} {apellido}, y tengo {edad} años.")

# usuario(nombre="Rafael", apellido="Vera", edad=22)
# usuario(nombre="Rafael", apellido="Vera")
#usuario(edad=22, apellido="Vera", nombre="Rafael")


# def suma(num1,num2):
#     result = num1 + num2
#     return result,num1,num2

# operacion,num1,num2 = suma(2,2)

# print(operacion,num1,num2)


def mayor(num1: int, num2: int) -> int:
    """Función que devuelve el mayor de dos números.

    Parametros
    ----------
    num1: int
        El primer número.
    num2: int
        El segundo número.
    
    Regresa
    -------
    int
        El número mayor de num1 y num2
    """
    if type(num1) is not int or type(num2) is not int:
        raise TypeError("Al menos un dato no es int")
    
    if num1 == num2:
        raise Exception("Los números son iguales")
    elif num1 > num2:
        return num1
    else:
        return num2


print(mayor(10, 20))
num1 = int(input("Ingresa el primer numero: "))
num2 = int(input("Ingresa el segundo numero: "))
print(mayor(num1, num2))

def suma(num1: float, num2: float) -> float:
    """Función que regresa la suma de dos números.

    Parametros
    ----------
    num1: float
        El primer número de la operación.
    num2: float
        El segundo número de la operación.
    
    Regresa
    -------
    float
        El resultado de la suma de num1 + num2
    """
    return num1 + num2


num1 = float(input("Ingresa el primer numero: "))
num2 = float(input("Ingresa el segundo numero: "))
print(suma(num1, num2))