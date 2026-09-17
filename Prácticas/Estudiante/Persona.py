class Persona:
  def saludar(self):
    return f"Hola, soy {self.nombre} y tengo {self.edad} años."
  def __init__(self, nombre, edad):
    self.nombre=nombre
    self.edad=edad