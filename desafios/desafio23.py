from abc import ABC, abstractmethod

class Poligono(ABC):
    def __init__(self, qnd_lados):
        self.qnd_lados = qnd_lados

    @abstractmethod
    def perimetro(self) -> float:
        pass

    @abstractmethod
    def area(self) -> float:
        pass

class Quadrado(Poligono):
    def __init__(self, lado = 2):
        super().__init__(4)
        self.lado = lado
    
    def perimetro(self):
        return self.lado*4
    
    def area(self):
        return self.lado ** 2
    
class Circulo(Poligono):
    def __init__(self, raio=3):
        super().__init__(0)

        self.raio = raio
    
    def perimetro(self):
        return 2 * self.raio * 3.14
    
    def area(self):
        return 3.14 * self.raio **2
    
p1 = Quadrado(12)
print(p1.area())
print(p1.perimetro())

p2 = Circulo(3)
print(p2.perimetro())
print(p2.area())