a = 10
b = 20

# Intercambio clasico
print(a, b)
aux = a
a = b
b = aux
print(a, b)

a = 10
b = 20

# Intercambio Pythonista
print(a, b)
a, b = b, a
print(a, b)

# Con tuplas
a, b = (1, 2)
print(a, b)