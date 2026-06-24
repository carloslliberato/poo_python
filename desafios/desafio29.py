from rich import inspect

class Diario:
    def __init__(self, senha='Hoje'):
        self.__senha = senha
        self.__segredos = []

    @property
    def senha(self):
        raise PermissionError('Ninguém tem permissão de ver a senha.')

    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, senha=None):
        if senha == self.__senha:
            print("## DIÁRIO ABERTO ##")
            for segredo in self.__segredos:
                print(segredo)
        else:
            print('Ninguém tem permissão de ver a senha')


d1 = Diario('Carlos')
inspect(d1, private=True, methods=True)
d1.escrever('Primeira mensagem')
d1.escrever('Você é uma pessoa simpatica')
d1.escrever('Você gosta de python')
inspect(d1, methods=True, private=True)
d1.ler('Carlos')