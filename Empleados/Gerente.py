from Empleado import Empleado
class Gerente(Empleado):
    def __init__(self, nombre, salario):
        super().__init__(nombre, salario)

    def calcular_salario(self):
        bono = self.salario * 0.30
        return self.salario + bono