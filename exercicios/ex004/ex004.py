from rich import print, inspect

class Pessoa:
    def __init__(self, nome='', idade=0):
        self.nome = nome
        self.idade = idade

    def fazer_aniversario(self):
        self.idade += 1
    
class Aluno(Pessoa):
    def __init__(self, nome, idade, curso, turma):
        super().__init__(nome, idade)
        self.curso = curso
        self.turma = turma
    
    def fazer_matricula(self):
        print("O aluno fez a matricula.")

class Professor(Pessoa):
    def __init__(self, nome, idade, especialidade, nivel):
        super().__init__(nome, idade)
        self.especialidade = especialidade
        self.nivel = nivel
    
    def dar_aula(self):
        print('O professor já deu aula')

class Funcionario(Pessoa):
    def __init__(self, nome, idade, cargo, setor):
        super().__init__(nome, idade)
        self.cargo = cargo
        self.setor = setor

    def bater_ponto(self):
        print("O funcionario bateu ponto")

a1 = Aluno('José', 17, 'Informática', 'T01')
inspect(a1, methods=True)
a1.fazer_aniversario()
a1.fazer_matricula()

p1 = Professor('Samuel', 56, 'Biologia', 'Mestre')
inspect(p1, methods=True)
p1.fazer_aniversario()
p1.dar_aula()

f1 = Funcionario('Claudia', 27, 'Coordenadora', 'Administrativo')
f1.fazer_aniversario()
f1.bater_ponto()