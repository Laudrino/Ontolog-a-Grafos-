from fractions import Fraction

# matriz 
matriz = [
    [0,   0,   1, 1/2, 1/3],
    [0, 0,   0,   0, 0],
    [0, 0  , 0,   0,   1/3],
    [0, 1/2, 0, 0,   0],
    [1,   1/2,   0, 1/2,   1/3]
]

# vector
vector = [
    [1/5],
    [1/5],
    [1/5],
    [1/5],
    [1/5]
]

# veces para multiplicar
n = 40

# matriz por el vector
for _ in range(n):
    resultado = [[sum(matriz[i][j] * vector[j][0] for j in range(len(matriz)))] for i in range(len(matriz))]
    vector = resultado

# resultado a fracción
resultado_fraccion = [[Fraction(item[0]).limit_denominator() for item in vector]]

# fracción
print("Resultado en fracción:")
for row in resultado_fraccion:
    print([f"{item.numerator}/{item.denominator}" for item in row])

# resultado a porcentaje
resultado_porcentaje = [[item[0] * 100 for item in vector]]

# porcentaje
print("\nResultado en porcentaje:")
for row in resultado_porcentaje:
    print([f"{item}%" for item in row])
