from Persona import Persona
class Estudiante(Persona):
  def info(self):
    return f"Soy {self.nombre} y estudio en el curso {self.curso}."
  def __init__(self, nombre, edad, curso):
    super().__init__(nombre, edad)
    self.curso=curso
    
      