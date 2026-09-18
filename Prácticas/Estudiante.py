#clase: el plano (molde)
class Estudiante:
    def __init__(self, nombre, edad, carrera): 
        self.nombre = nombre
        self.edad = edad
        self.carrera = carrera
        
#objetos: instancias concretas (casas construidas)
juan = Estudiante("Juan Pérez", 18, "Ingeniería")
maria = Estudiante("María Gómez", 19, "Medicina")

print(juan.nombre) #salida: Juan Pérez
print(maria.carrera) #salida: Medicina