#Scope
animal = 'León' #Variable global -> Funcion, condicion o ciclo

def imprimir_animal():
    global animal
    animal='Gato'

    #animal = 'Ballena' #Variable local
    tipo = 'Mamifero' #Variable local
    print(animal)
    print(id(animal))

imprimir_animal()
print(animal)
print(id(animal))