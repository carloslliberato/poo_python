# Crie a classe Gamer, onde podemos cadastrar nome, nick e os jogos favoritos de uma pessoa.
# Crie tabmém um método que permita mostrar a ficha desse gamer.

from rich.panel import Panel
from rich import print

class Gamer:
    def __init__(self, nome, nick):
        self.nome = nome
        self.nick = nick
        self.favoritos = list()
    
    def add_favoritos(self, nomeJogo):
        self.favoritos.append(nomeJogo)
        self.favoritos = sorted(self.favoritos, key=str.lower)

    def ficha(self):
        conteudo = f"Nome real: {self.nome}"
        conteudo += f"\nJogos Favoritos:"
        for num, game in enumerate(self.favoritos):
            conteudo += f"\n:video_game: {game}"
        panel = Panel(conteudo, width=30, title=self.nick)
        print(panel)

j1 = Gamer('Olívia Souza', 'peach_raivosa')
j1.add_favoritos('Mario Bross')
j1.add_favoritos('Call of Duty')
j1.ficha()