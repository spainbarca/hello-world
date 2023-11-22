nombre = 'Noah'
apellido = 'Martinez'

# Usando "+" para concatenar
print(nombre + ' '+ apellido)

# Usando %s (reemplazo de valores)
nombre_completo = 'Mr. %s %s %s.' %(nombre, apellido, 'Hancco')
print(nombre_completo)

# Usando format
nombre_completo = 'Ing. {} {}.'.format(nombre,apellido)
print(nombre_completo)

nombre_completo = 'Ing. {nombre} {primer_app} {segundo_ap}.'.format(
    nombre=nombre,
    primer_app=apellido,
    segundo_ap='Hancco'
)
print(nombre_completo)