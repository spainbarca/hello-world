def promedio(*args):
    print(args)
    print(type(args))
    return sum(args)/len(args)

resul_prom = promedio(14, 20, 12, 16, 13)
print(resul_prom)