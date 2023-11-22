titulo_curso='Curso profesional de Python, donde veremos Python 3.11'

# .count retorna la cantidad de coincidencias dentro de un string
contador = titulo_curso.count('Python')
print(contador)

contador = titulo_curso.count('o')
print(contador)

# Saber si existe o no esa cadena en la variable
print("Python" in titulo_curso)

# lower() para pasar a minusculs
print("python" in titulo_curso.lower())

# startswith para saber con que palabra inicia la cadena
print(titulo_curso.startswith('curso'))

# endsith para saber si esa palabra está al final de la cadena
print(titulo_curso.endswith('3.11'))