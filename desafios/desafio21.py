# Crie a classe Caneta, que simule o funcionamento de uma caneta colorida, pdoendo escrever frases com a cor relativa
from rich import print
class Caneta:
    def __init__(self, cor = 'blue'):
        self.cor = cor
        self.estaDestampada = False

    def destampar(self):
            self.estaDestampada = True
    
    def tampar(self):
            self.estaDestampada == False

    def escrever(self, frase):
        if self.estaDestampada == False:
            return "A caneta está tampada!"
        
        return f"[{self.cor}]{frase}[/]"
    
    def quebrarLinha(self, qnt=1):
         print("\n"*qnt, end="")

c1 = Caneta('purple')
c2 = Caneta('red')

c1.destampar()
print(c2.escrever('Oi, testando caneta 2'))
print(c1.escrever('Oi, testando caneta 1'))
c2.destampar()
c2.quebrarLinha(2)
print(c2.escrever('Oi, testando caneta 2'))
