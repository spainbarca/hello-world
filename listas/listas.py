# Las sublistas son una extraccion de la lista en cuestión
# Los´índices en python comienzan en 0

#               0           1       2       3       4
lista_cursos = ['Python', 'Flask','SQL','Laravel','Java']

#[start:end]
sub_lista = lista_cursos[1:4]
print(sub_lista)

#a partir de [start:]
sub_lista = lista_cursos[3:]
print(sub_lista)

#hasta el [:end]
sub_lista = lista_cursos[:1]
print(sub_lista)

#[start:end:skip]
sub_lista = lista_cursos[1:5:2]
print(sub_lista)

#[:]
sub_lista = lista_cursos[:]
print(sub_lista)