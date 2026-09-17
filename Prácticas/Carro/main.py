from Vehiculo import Vehiculo
from Coche import Coche

coche = Coche("Toyota", 4)
print(f"Marca: {coche.marca}, Puertas: {coche.num_puertas}")
coche.arrancar()