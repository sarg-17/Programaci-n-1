from Figuras import Figuras
import math

class Circulo(Figuras):
    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return math.pi * (self.radio ** 2)