from Figuras import Figuras
from Circulo import Circulo
from Rectangulo import Rectangulo
from Triangulo import Triangulo

mis_figuras = [
    Rectangulo(5, 10),   
    Circulo(7),          
    Triangulo(6, 4)      
]

print("ÁREAS DE LAS FIGURAS")
for figura in mis_figuras:
    nombre_figura = type(figura).__name__
    resultado_area = figura.area()
    print(f"{nombre_figura}: {resultado_area:.2f}")