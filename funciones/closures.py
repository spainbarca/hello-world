e = 'e' # Variable global

def funcion_principal():
    a = 'a'
    b = 'b'

    def funcion_anidada():
        c = 'c' # Variable local

        nonlocal b #Usar una var local que se encuentre en nivel superior
        b = 'Cambio de valor'

        print(a)
        print(b)
        print(id(b))

        print(e)

    funcion_anidada()
    #print(c)
    print(b)
    print(id(b))

funcion_principal()