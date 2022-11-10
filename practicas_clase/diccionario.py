diccionario = {1,3,4}
print(type(diccionario))

diccionario2 = {
    'dato1':2,
    'dato2':"numero2",
    'booleano':True,
    'flotante':3.14,
    'lista':[12,123,545],
    'diccionario':{
        'dichijo':1,
        'dichijo2':2}
    }

# print(diccionario2['booleano']) 
# bul = diccionario2['booleano']
print(diccionario2.keys())
print(diccionario2.values())