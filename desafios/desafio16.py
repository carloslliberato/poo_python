# Crie uma classe Funcionario, onde podemos cadastrar Nome, Setor e Cargo.
# Crie tambem um método que permita ao funcionário se apresentar

from rich import print

class Funcionario:
    """
Cria um funcionário com nome, setor e cargo com o método de se apresentar.
    """
    empresa = 'PUC Campinas'
    def __init__(self, nome, setor, cargo):
        self.nome = nome
        self.setor = setor
        self.cargo = cargo
    
    def apresentar(self):
        return f"Olá, sou {self.nome} do setor {self.setor}, sou {self.cargo} da {Funcionario.empresa}, muito prazer !"

f1 = Funcionario('Carlos', 'Desenvolvimento', 'Programador Júnior')
print(f"{f1.apresentar()} :+1:")