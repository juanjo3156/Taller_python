dividendo = int(input("Ingresa un numero a dividir: "))
divisor = int(input("Ingresa un numero que divida: "))

if divisor == 0:
    print("No puedes dividir con 0")
else:
    resultado = dividendo//divisor
    print(f"El resultado de la división es: {resultado}")


# if 5 > 2 and 5>9:
#     print("hola")