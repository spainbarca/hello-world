# * como prefijo -> lista
numeros = (1,2,3,4,5,6)
uno, dos, tres, cuatro, *resto_valores = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(resto_valores)


# _ indica que no deseamos trabajar con ellos (omitir valor)
numeros = (1,2,3,4,5,6)
uno, dos, tres, cuatro, *_ = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)


# se le añada comas despues de _, para considerar los ultimos valores que si
numeros = (1,2,3,4,5,6,7,8,9,10)
uno, dos, tres, cuatro, *_,nueve,diez = numeros

print(uno)
print(dos)
print(tres)
print(cuatro)
print(nueve)
print(diez)


# se colocan _ durante la estructura pra omitir algunos numeros q no nos interesan
numeros = (1,2,3,4,5,6,7,8,9,10)
uno, _, tres, cuatro, *_,nueve,_ = numeros

print(uno)
print(tres)
print(cuatro)
print(nueve)
print(diez)