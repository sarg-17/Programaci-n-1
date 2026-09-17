from Animal import Animal
class Vaca(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} ({self.edad} años) dice: ¡Muuuu!")