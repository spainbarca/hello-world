diccionario = {'a':1,'b':2,'c':3,'d':4}
print(len(diccionario))

del diccionario['a']

print(diccionario)
print(len(diccionario))


# pop
valor = diccionario.pop('b')
print(diccionario)
print(len(diccionario))


#clear
valor = diccionario.clear()
print(diccionario)
print(len(diccionario))