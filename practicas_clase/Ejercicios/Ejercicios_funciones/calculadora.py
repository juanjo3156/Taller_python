def suma():
    num1 = float(input("ingresa el primer numero: "))
    num2 = float(input("ingresa el segundo numero: "))
    resultado = num1+num2
    print(resultado)

def resta():
    num1 = float(input("ingresa el primer numero: "))
    num2 = float(input("ingresa el segundo numero: "))
    resultado = num1-num2
    print(resultado)

def multi():
    num1 = float(input("ingresa el primer numero: "))
    num2 = float(input("ingresa el segundo numero: "))
    resultado = num1*num2
    print(resultado)


def division():
    num1 = float(input("ingresa el primer numero: "))
    num2 = float(input("ingresa el segundo numero: "))
    resultado = num1/num2
    print(resultado)
continuar = True
while continuar:
    opcion = input("Qué quieres hacer 1.para sumar, 2.para restar,3.para multiplicar, 4.para dividir: ")

    if opcion == "1":
        suma()
        seguir = input("quieres hacer otra operaciónn?")
        if seguir == "yes":
            continuar = True
        elif seguir == "no":
            continuar = False
    elif opcion == "2":
        resta()
        seguir = input("quieres hacer otra operaciónn?")
        if seguir == "yes":
            continuar = True
        elif seguir == "no":
            continuar = False
    elif opcion == "3":
        multi()
        seguir = input("quieres hacer otra operaciónn?")
        if seguir == "yes":
            continuar = True
        elif seguir == "no":
            continuar = False
    elif opcion == "4":
        division()
        seguir = input("quieres hacer otra operaciónn?")
        if seguir == "yes":
            continuar = True
        elif seguir == "no":
            continuar = False
    else: 
        print("ingresa una opcion valida")





