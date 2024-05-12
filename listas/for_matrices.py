matriz= [
    [14,13,14,26,7],
    [20,147,12,36,7]
]

for fila in matriz:
    for elemento in fila:
        print(elemento, end=" ")
    print()


print()

for i in range(0, len(matriz)):
    for j in range(0, len(matriz[i])):
        print(matriz[i][j], end=" ")
    print()