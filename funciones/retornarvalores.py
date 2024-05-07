def suma(a,b):
    return a+b, 'La funcion retorna 2 valores'

n1 = int(input('Ingresa el primer número entero: ')) #string
n2 = int(input('Ingresa el segundo número entero: '))

result, message=suma(n1,n2)
print('El resultado es: ',result)
print('El mensaje es: ',message)