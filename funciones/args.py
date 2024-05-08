def promedio(*args):
    print(args)
    print(type(args))
    return sum(args)/len(args)


def combinacion(p1, p2, *args, p4):
    print(p1)
    print(p2)
    print(args)
    print(p4)

resul_prom = promedio(14, 20, 12, 16, 13)
print(resul_prom)

combinacion(10,25,14,12,14,58,p4=100)