def usuarios(**kwargs): #dict
    print(kwargs)
    print(type(kwargs))


usuarios(eduardo=[10,15,13], fernando=[16,14,13])


def combinacion(*args, **kwargs):
    print(args)
    print(kwargs)


combinacion(1,2,3,4,5, noah=True, curso='Python')