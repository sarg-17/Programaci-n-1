from Empleado import Empleado
from Gerente import Gerente

class Vendedor(Empleado):
    def __init__(self, nombre, salario, ventas):
        super().__init__(nombre, salario)
        self.ventas = ventas

    def calcular_salario(self):
        comision = self.ventas * 0.10
        return self.salario + comision