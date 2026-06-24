from abc import ABC, abstractmethod
import random

class Personagem(ABC):
    def __init__(self, nome, vida):
        self.nome = nome
        self.vida = vida
        self.golpes = []

    def atacar(self, alvo, forca):
        if self.vida > 0 and alvo.vida > 0:
            golpe = self.golpes[random.randrange(0, len(self.golpes))]
            print(f'{self.nome}({self.vida}) atacou {alvo.nome}({self.vida}) com {golpe} de {forca} de dano')
            alvo.receber_dano(forca)
        else:
            print(f"O ataque do {self.nome}({self.vida}) -> {alvo.nome}({self.vida}) não pode acontecer")

    def receber_dano(self, dano):
        fator = random.randint(0, dano)
        self.vida -= fator
        if self.vida < 0:
            self.vida = 0
        print(f"O personagem {self.nome} recebeu {fator} de dano.")

    @abstractmethod
    def curar(self):
        pass
        
class Guerreiro(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Soco', 'Machado', 'Chute']

    def curar(self):
        fator = random.randint(1, self.vida)
        self.vida += fator
        print(f'{self.nome} curou {fator} de vida.')



class Mago(Personagem):
    def __init__(self, nome, vida):
        super().__init__(nome, vida)
        self.golpes = ['Bolsa de Fogo', 'Raio de Luz', 'Choque']

    def curar(self):
        fator = random.randint(1, 100)
        self.vida += fator
        print(f'{self.nome} usou uma poção e curou {fator} de vida.')
