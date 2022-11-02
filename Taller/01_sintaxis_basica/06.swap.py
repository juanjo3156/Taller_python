""" El metodo 'swap' """

# Intercambio de variables de forma convencional
var_1 = "Texto 1"
var_2 = "Texto 2"

aux = var_1
var_1 = var_2
var_2 = aux

print("Forma convencional:")
print("Variable 1: "+var_1, "Variable 2: "+var_2, sep="\n", end="\n\n")

# Intercambio de variables de forma pythonista
var_1 = "Texto 1"
var_2 = "Texto 2"

var_1, var_2 = var_2, var_1

print("Forma pythonista")
print("Variable 1: "+var_1, "Variable 2: "+var_2, sep="\n")