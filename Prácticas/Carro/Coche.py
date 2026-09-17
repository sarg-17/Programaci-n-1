from Vehiculo import Vehiculo

class Coche(Vehiculo):
  def __init__(self, marca, num_puertas):
    super().__init__(marca)
    self.num_puertas = num_puertas