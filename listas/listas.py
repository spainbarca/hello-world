# Basta con colocar la funcion list() o corchetes
# Los´índices en python comienzan en 0

#lista = list(1,3.14,'Perucito',False)
lista = [1,3.14,'Perucito',False]

lista_strings = ['Juan', 'Rojas','Sky']
lista_cursos = ['Python', 'Flask','SQL','Laravel','Java']
lista_enteros = [14,12,34,-1]
lista_floats = [14.2, 12.25,144.6]
lista_booleanos = [True, False, (1 > 1)]

# Actualizar registro de lista
lista_cursos[4] = 'Rust'

print(lista_cursos[4])