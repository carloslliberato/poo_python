# Crie a classe Produto, onde podemos cadastrar Nome e o Preco.
# Crie também um método que mostre uma etiqueta de preco do produto.

from rich.panel import Panel
from rich import print

class Produto:

    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def etiqueta(self):
        conteudo = f"{self.nome.center(30, ' ')}"
        conteudo += f"{'-'*30}"
        precoF = f"R${self.preco:,.2f}"
        conteudo += f"{precoF.center(30, '.')}"
        painel = Panel(f"{conteudo}", title='Produto', width=34)
        print(painel)

p1 = Produto('iPhone 17 Pro Max', 25000.00)
p2 = Produto('Notebook Gamer', 8000)

p1.etiqueta()
p2.etiqueta()