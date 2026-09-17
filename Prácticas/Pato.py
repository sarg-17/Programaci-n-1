class Nadador:
    def nadar(self):
        print("🤽‍♀️ Nadando")

class Volador:
    def volar(self):
        print("🪽 Volando")

class Pato(Nadador, Volador):
    def __init__(self, nombre):
        self.nombre=nombre
    
    def graznar(self):
        print("🦆 ¡Cuac!")
        
pato=Pato("Lucas")
pato.nadar()
pato.volar()
pato.graznar()         