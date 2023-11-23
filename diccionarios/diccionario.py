elementos = {}

elementos['nombre'] = 'Cody' # Crea la llave
elementos[(1, 2 , 3)] = 'La llave es una tupla'

# Si la llave no existe, la crea, caso conmtrario, la actualiza
elementos['nombre'] = 'Codigo Facilito'

print(elementos)
print(len(elementos))


elementos = {'a':1,'b':2,'c':3,'a':4}
print(elementos)