#Metodos de analisis 
texto = "Bienvenidos al imalaya"

#count
print("======COUNT=======")
print(texto.count("Bienvenidos"),"\n")

#find() 
print("======FIND========")
print(texto.find("al"),"\n")

#index()
print("======INDEX=======")
print(texto.index("al"),"\n")

#rfind() rindex() lo mismo pero buscan a la inversa

#rftind()
print("======RFIND=======")
print(texto.rfind("al"),"\n")
#rindex()
print("======RINDEX======")
print(texto.rindex("al"),"\n")

#startswith()
print("====STARTSWITH====")
print(texto.startswith("Bienvenidos"),"\n")
print(texto.startswith("imalaya"),"\n")

#endswith()
print("====ENDSWITH====")
print(texto.endswith("Bienvenidos"),"\n")
print(texto.endswith("imalaya"),"\n")

#Metodos de transformación
texto2 = "cacHoRrito"
print("====CAPITALIZE====")
print(texto2.capitalize(),"\n")

#Lower y Upper
print("====LOWER====")
print(texto2.lower(),"\n")

print("====UPPER====")
print(texto2.upper())

#swapcase
print("====SWAPCASE====")
print(texto2.swapcase())

#replace 
print("====REPLACE====")
print(texto2.replace('cacHoRrito','Grande'))

#Metodos de separación y unión
print("====SPLIT====")
texto3 = "perro bravo no se acerque"
print(texto3.split(" "))


#Convierte una lista en una cadena de texto
lista = ["hola","como estas?"]
cadena_join = " ".join(lista)
print(cadena_join)
#dir nos permite conocer los metodos que se pueden utilizar en disdintos datos
# print(dir(texto3))