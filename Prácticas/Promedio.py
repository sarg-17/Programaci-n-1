matriz = []

for i in range(3):
    numero = float(input(f"Ingresa el número {i + 1}: "))
    matriz.append(numero)

suma = sum(matriz)
division = suma/3
print("Matriz resultante:", matriz)
print("Tu promedio es: ", division)