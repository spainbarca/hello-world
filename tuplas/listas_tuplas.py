cursos = ['PHP', 'Java', 'C#', 'JavaScript', 'Dart']
niveles = ('Basico','Intermedio','Avanzado')

# tuple() para generar una tupla en base a una lista
cursos_tupla = tuple(cursos)
print(cursos_tupla)
print(type(cursos_tupla))

# list() para generar una lista en base a una tupla
niveles_lista = list(niveles)
print(niveles_lista)
print(type(niveles_lista))