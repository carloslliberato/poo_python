from abc import ABC, abstractmethod

class Transporte(ABC):
    def __init__(self, dist):
        self.dist = dist
        self.frete = 0

    @abstractmethod
    def calc_frete(self):
        pass


class Moto(Transporte):
    fator = 0.5
    def __init__(self, dist):
        super().__init__(dist)
    
    def calc_frete(self):
        self.frete = Moto.fator * self.dist
        return f'R${self.frete:,.2f}'


class Caminhao(Transporte):
    fator = 1.20
    def __init__(self, dist):
        super().__init__(dist)

    def calc_frete(self):
        if self.dist >= 50:
            self.frete = Caminhao.fator * self.dist
            return f'R${self.frete:,.2f}'
        else:
            self.frete = 0
            return "Percurso de Caminhão mínimo 50Km" 
    

class Drone(Transporte):
    fator = 9.50
    def __init__(self, dist):
        super().__init__(dist)

    def calc_frete(self):
        if self.dist <= 10:
            self.frete = Drone.fator * self.dist
            return f'R${self.frete:,.2f}'
        else:
            self.frete = 0
            return "Percurso de Drone máximo de 10Km"

# entrega = Drone(10)
# print(entrega.calc_frete())