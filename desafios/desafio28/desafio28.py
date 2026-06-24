class Termostato:
    def __init__(self, temperatura = 20):
        self.__temperatura = temperatura
        self.ftemperatura = f'{self.temperatura}°C'

    @property
    def temperatura(self):
        return self.__temperatura
    
    @temperatura.setter
    def temperatura(self, valor):
        if 16 <= valor <= 30 and round(valor % 0.5) == 0:
            self.__temperatura = valor
        else:
            print("Temperatura Inválida")
