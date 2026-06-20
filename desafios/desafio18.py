# Crie a classe Churrasco, onde seja possivel informar quantas pessoas vão participar.
# E mostre quanta carne deve ser comprado, o custo total do churras co e o preço por pessoa
from rich.panel import Panel
from rich import print
class Churrasco:
    consumo = 0.4
    preco = 82.40

    def __init__(self, nome, pessoas):
        self.nome = nome
        self.pessoas = pessoas

    def calcularCarne(self) -> float:
        return Churrasco.consumo * self.pessoas
    
    def calcularCustoTotal(self) -> float:
        return self.calcularCarne() * Churrasco.preco
    
    def calcularCustoIndividual(self) -> float:
        return self.calcularCustoTotal() / self.pessoas

    def analisar(self):
        conteudo = f'Analisando [green]{self.nome}[/] com [blue]{self.pessoas} convidados[/]'
        conteudo += f'\nCada participante comerá {Churrasco.consumo}Kg e cada Kg custa R${Churrasco.preco:,.2f}'
        conteudo += f'\nRecomendo [blue]comprar {self.calcularCarne():,.3f}Kg[/] de carne'
        conteudo += f'\nO custo total será de [green]R${self.calcularCustoTotal():,.2f}[/].'
        conteudo += f'\nCada pessoa pagará [yellow]R${self.calcularCustoIndividual():,.2f}[/] para participar.'
        painel = Panel(conteudo, title=self.nome, width=70)

        print(painel)

c1 = Churrasco('Churras dos Amigos', 15)
c1.analisar()