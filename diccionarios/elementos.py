diccionario = {'a':1,'b':2,'c':3,'d':4}

valor = diccionario['d']
print(valor)

print('a' in diccionario)

# get, para obtener un valor de manera segura
valor = diccionario.get('d')
print(valor)

valor = diccionario.get('z')
print(valor)


# setDefault
valor = diccionario.get('z', 'La llave no existe en el diccionario')
print(valor)
