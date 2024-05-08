def pares(): # -> Lazy itirator
    for numero in range(0,16,2):
        yield numero # La funcion suspende su ejecucion
        print ("Se reanuda la ejecucion")

generador = pares()

while True:
    try:
        par = next(generador)
        print(par)
    except StopIteration:
        print("el generador finalizó")
        break