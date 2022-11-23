#para declarar funciones usamos la parabra areservada def
def funcion1():
    print("soy una función")

funcion1()

#podemos darles argumentos a las funciones

# def hola_nombre(nombre):
#     print(f"Hola {nombre} ¿cómo estas?")

# hola_nombre("Juan")


#tambien podemos definir los parametros de la función

# def usuario(nombre, apellido, edad=0):
#     print(f"Hola, soy {nombre} {apellido}, y tengo {edad} años.")

# usuario(nombre="Rafael", apellido="Vera", edad=22)
# usuario(nombre="Rafael", apellido="Vera") #podemos cambiar ciertos valores de argumentos que ya tengan un valor por defecto


#sentencia return 
#con la sentencia return podemos obtener un valor a partir de una función 
# def suma(num1,num2):
#     return num1 + num2
    
# print(suma(2,2))

#retornar valores multiples
def nombres(nombre1,nombre2):
    return nombre1, nombre2

print(nombres("Juan","Arturo"))


#listas como argumento
# lista = [1,2,3]
# def listar (iterable):
#     return iterable

# print(listar(lista))

#