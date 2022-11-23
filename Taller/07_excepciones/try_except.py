
#el bloque try dara error porque x no esta definida

# try:
#   print(x)
# except NameError:
#   print("Eso no es posible mejor te imprimo un 4")
#   print(4)


# try:
#   print(x)


# except NameError:
#   print("Variable x no definida")

# except:
#   print("Algo fue mal")
  



# try:
#   print("Hola")
# except:
#   print("Algo va mal")
# else:
#   print("Ningun error")
#   op = input("jeje: ")

# try:
#   print(1)
# except:
#   print("Algo va mal")
# finally:
#   print("el bloque try/except finalizo")


x = 0

if x == 0:
  raise Exception("X no puede ser 0")