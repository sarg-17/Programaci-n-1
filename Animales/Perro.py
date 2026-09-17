from Animal import Animal
class Perro(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} ({self.edad} años) dice: ¡Guau guau!")