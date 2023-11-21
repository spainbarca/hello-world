lista_cursos = ['Python', 'Flask','SQL','Laravel','Java']
lista_cursos2 = ['Docker', 'Kubernetes','MongoDB']

# .append para añadir nuevos elementos
lista_cursos.append('PHP')
lista_cursos.append('C#')
lista_cursos.append('R')

# .len para saber la longitud de la lista
print(len(lista_cursos))

# .insert añadir elemento desde un indice exacto
lista_cursos.insert(1,'CodeIgniter')

# .extend para añadir una lista dentro de otra (unir)
lista_cursos.extend(lista_cursos2)
print(lista_cursos)

# .remove para eliminar un elemento de una lista
lista_cursos.remove('Kubernetes')
print(lista_cursos)

# del, para eliminar un elemento de un array basado en indices
del lista_cursos[1]
print(lista_cursos)

# .clear para eliminar todos los elementos de una lista
lista_cursos.clear()
print(lista_cursos)