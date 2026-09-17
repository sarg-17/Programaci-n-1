class Animal:
    def sonido(self):
        print("Sonido genérico")
        
class Perro(Animal):
    def sonido(self):
        print("🐕 ¡Guau!")
        
class Gato(Animal):
    def sonido(self):
        print("🐈¡Miau!")
        
animales = [Perro(), Gato(), Animal()]
for animal in animales:
     animal.sonido()          