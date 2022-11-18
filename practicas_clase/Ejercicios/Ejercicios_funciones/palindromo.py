# Solución ejercicio palíndromo
def palindromo(texto):
    texto_formateado = texto.lower().replace(" ", "")
    if texto_formateado == texto_formateado[::-1]:
        print("Es un palíndromo :D")
    else:
        print("No es un palíndromo D:")

#texto_input = input("Ingresa una frase o palabra: ")
#palindromo(texto_input)