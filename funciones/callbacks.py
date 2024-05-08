promedio = lambda *args : sum(args)/len(args)

aprobado = lambda calificacion : calificacion >= 12.5

#print (promedio(14,12,19,20,16))
#print (aprobado(14))

def mostrar_mensaje(func_prom, func_aprob, *args):
    promedio = func_prom(*args)

    if func_aprob(promedio):
        print(f"Felicitaciones, aprobaste el curso con {promedio}")
    else:
        print("No aprobaste el curso")


mostrar_mensaje(promedio, aprobado, 10,12,18,16,17,8)