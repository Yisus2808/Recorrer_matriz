# Recorre la matriz numérica e imprime sus valores y posición donde sean mayores a 4.											

matriz = [
            [1,5,3,7,4],
            [7,8,6,4,5],
            [9,2,8,3,4]
        ]

mayor = 4
new_matriz = []
posicion = []

for fila in matriz:
    for i, valor in enumerate(fila):
        if valor > mayor:
            new_matriz.append(valor)
            posicion.append(i)

print("De la matriz: ")
print(matriz)
print("Los mayores a 4 son: ")
print(new_matriz)
print("Y sus posiciónes son: ")
print(posicion)