lenguajes = "Python Ruby Java Rust C++ C"

# .split para crear una lista de una cadena, por las separaciones de espacios
listado_lenguajes = lenguajes.split()
print(listado_lenguajes)

# .split se le coloca el caracter de separacion dentro de los parentesis
lenguajes = "Python_Ruby_Java_Rust_C++_C"
listado_lenguajes = lenguajes.split("_")
print(listado_lenguajes)

listado_lenguajes = lenguajes.split("_",3)
print(listado_lenguajes)


lenguajes = ["Python", "Ruby", "Java", "Rust", "C++", "C"]

# .join para unir en un string los elementos de una lista
string_lenguajes = ' - '.join(lenguajes)
print(string_lenguajes)
