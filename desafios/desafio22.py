# Crie a classe ControleRemoto, onde vamos imular o funcionamento de um controle simples
# (canal, volume e ligar/desligar)
from rich.panel import Panel
from rich import print

class ControleRemoto:
    canal_min:int = 1
    canal_max:int = 6
    volume_min:int = 1
    volume_max:int = 5

    def __init__(self, canal=1, volume=2):
        self.canal_atual:int = canal
        self.volume_atual:int = volume
        self.ligado:bool = False

    def ligar_desliga(self):
        self.ligado = not self.ligado

    def canal_mais(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_max:
                self.canal_atual = ControleRemoto.canal_min
            else:
                self.canal_atual+=1

    def canal_menos(self):
        if self.ligado:
            if self.canal_atual == ControleRemoto.canal_min:
                self.canal_atual = ControleRemoto.canal_max
            else:
                self.canal_atual-=1

    def volume_mais(self):
        if self.ligado:
            if self.volume_atual == ControleRemoto.volume_max:
                self.volume_atual = ControleRemoto.volume_min
            else:
                self.volume_atual+=1
    def volume_menos(self):
        if self.ligado:
            if self.volume_atual == ControleRemoto.volume_min:
                self.volume_atual = ControleRemoto.volume_max
            else:
                self.volume_atual-=1

    def mostrarTv(self):
        conteudo = ''
        if not self.ligado:
            conteudo = f':prohibited:A tv esta desligada'
        else:
            conteudo = f'CANAL  = '
            for canal in range(ControleRemoto.canal_min, ControleRemoto.canal_max+1):
                if canal == self.canal_atual:
                    conteudo += f' [yellow on yellow] {canal} [/] '
                else:
                    conteudo += f' {canal} '
            
            conteudo += f'\nVOLUME = '
            for volume in range(ControleRemoto.volume_min, ControleRemoto.volume_max+1):
                if volume <= self.volume_atual:
                    conteudo += f'[black on cyan] [/]'
                else:
                    conteudo += f'[black on white] [/]'

        tv = Panel(conteudo, title='[ TV ]', width=50)
        print(tv)

c = ControleRemoto(1, 4)
while True:
    c.mostrarTv()
    comando = input(f'\n < CH >   - VOL +  ')
    match comando:
        case '0': break
        case '@': c.ligar_desliga()
        case '>': c.canal_mais()
        case '<': c.canal_menos()
        case '-': c.volume_menos()
        case '+': c.volume_mais()
    print('\n'*10)