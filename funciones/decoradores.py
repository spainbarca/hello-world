"""
a -> La funcion principal (Decorador)
b -> La función de decorar
c -> La función decorada

a(b) -> c
"""

def funcion_a(funcion_b):

    def funcion_c(*args, **kwargs):
        print('>>> Antes del llamado')
        
        result = funcion_b(*args, **kwargs)
        
        print('>>> Después del llamado')

        return result

    return funcion_c


#@funcion_a
#def saludar():
#    print ('Hola, estamos en una función')

@funcion_a
def suma(n1, n2):
    return n1 + n2

resultado = suma(15, 39)
print(resultado)