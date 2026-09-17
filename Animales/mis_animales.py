from Animal import Animal
from Perro import Perro
from Vaca import Vaca
from Gato import Gato

mis_animales = [
    Perro("Rex", 5),
    Gato("Luna", 2),
    Vaca("Lola", 4)
]

for animal in mis_animales:
    animal.hacer_sonido()