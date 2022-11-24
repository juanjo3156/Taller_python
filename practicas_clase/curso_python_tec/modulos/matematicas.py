"""Modulo encargado de las operaciones algebraicas básicas.
"""


def suma(
    num1: float = 0,
    num2: float = 0) -> float:
    """Función que regresa la suma de dos números.
    Por defecto los valores de los números son 0 (cero).
    
    Parametros
    ----------
    num1: float
        El primer número de la operación.
    num2: float
        El segundo número de la operación.
    
    Regresa
    -------
    float
        El resultado de la suma del primer número con el segundo.
    """
    return num1 + num2


def resta(
    minuendo: float = 0,
    sustraendo: float = 0) -> float:
    """Función que regresa la resta de dos números.
    Por defecto los valores de los parámetros son 0 (cero).
    
    Parametros
    ----------
    minuendo: float
        El valor base de la operación.
    sustraendo: float
        El valor a restar al minuendo.
    
    Regresa
    -------
    float
        La diferencia entre el minuendo y el sustraendo.
    """
    return minuendo - sustraendo


def multiplicacion(
    multiplicando: float = 1,
    multiplicador: float = 1) -> float:
    """Función que regresa la multiplicacion de dos números.
    Por defecto los valores de los parámetros son 1 (uno).
    
    Parametros
    ----------
    multiplicando: float
        El valor base de la operación.
    multiplicador: float
        El valor por el que se multiplicará.
    
    Regresa
    -------
    float
        El multiplicando sumado a sí mismo la misma
        cantidad que el valor del multiplicador.
    """
    return multiplicando * multiplicador


def division(
    dividendo: float = 1,
    divisor: float = 1) -> float:
    """Función que regresa la división de dos números.
    Por defecto los valores de los parámetros son 1 (uno).
    
    Parametros
    ----------
    dividendo: float
        El valor base de la operación.
    divisor: float
        El valor por el que se dividirá la operación.
    
    Regresa
    -------
    float
        El cociente de la operación.
    """
    if divisor == 0:
        raise ZeroDivisionError("El divisor no debe ser cero.")
    
    return dividendo / divisor