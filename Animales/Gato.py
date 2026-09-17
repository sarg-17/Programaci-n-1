from Animal import Animal
class Gato(Animal):
    def hacer_sonido(self):
        print(f"{self.nombre} ({self.edad} años) dice: ¡Miau miau!")