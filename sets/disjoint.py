lista1 = {1,3,5,10,47,26}
lista2 = {11,17,49,4,53,0}

todo_lista=lista1.union(lista2)
print(todo_lista)

print(lista1.isdisjoint(lista2))

todo_lista=lista1.intersection(lista2)
print(todo_lista)
print()



lista3 = {"PHP","Java","Python"}
lista4 = {"Java","C#","C++"}

todo_lista2=lista3.union(lista4)
print(todo_lista2)

print(lista3.isdisjoint(lista4))

todo_lista2=lista3.intersection(lista4)
print(todo_lista2)