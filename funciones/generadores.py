def pares(): # -> Lazy itirator
    for numero in range(0,100,2):
        yield numero # La funcion suspende su ejecucion

for par in pares():
    print(pares())