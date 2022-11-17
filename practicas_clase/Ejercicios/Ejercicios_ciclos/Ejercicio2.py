edad = int(input("Ingresa tu edad: "))

for i in range(edad):
    if i+1 == 1:
        print(f"Tengo {i+1} año")
    else:
        print(f"Tengo {i+1} años")
