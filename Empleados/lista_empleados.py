from Empleado import Empleado
from Gerente import Gerente
from Vendedor import Vendedor

lista_empleados = [
    Empleado("Ana", 1000),              
    Gerente("Carlos", 2000),            
    Vendedor("Luis", 1200, 5000)        
]

print("NÓMINA DE EMPLEADOS")
for empleado in lista_empleados:
    nombre_cargo = type(empleado).__name__
    salario_final = empleado.calcular_salario()
    print(f"{empleado.nombre} ({nombre_cargo}): ${salario_final:.2f}")
