num1 = float(input("Primer número: "))
num2 = float(input("Segundo número: "))
operacion = input("+ ó - ")
if operacion == "+":
    resultado = num1 + num2
    print(f"Resultado: {num1} + {num2} = {resultado}")
elif operacion == "-":
    resultado = num1 - num2
    print(f"Resultado: {num1} - {num2} = {resultado}")
else:
    print("Operación no valida")