def area_circulo(radio, pi=3.14):
    return pi*(radio ** 2)

rad=float(input('Indica el radio del circulo: '))

resultado = area_circulo(rad)
print(resultado)