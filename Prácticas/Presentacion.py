class Persona:
    # Constructor (inicializa los atributos)
    def __init__(self, nombre, edad):
        self.nombre = nombre #atributo público
        self.__edad = edad #atributo privado (encapsulamiento)
    
    #método 
    def saludar(self):
        print(f"Hola, me llamo {self.nombre}.")

#instanciar un objeto        
persona1 = persona = Persona("Carlos", 30)
persona1.saludar()