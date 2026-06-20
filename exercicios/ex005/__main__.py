from rich import inspect
from aluno import Aluno
from professor import Professor
from funcionario import Funcionario

def main():
    a1 = Aluno('José', 17, 'Informática', 'T01')
    # inspect(a1, methods=True)
    a1.fazer_aniversario()
    a1.fazer_matricula()

    p1 = Professor('Samuel', 56, 'Biologia', 'Mestre')
    # inspect(p1, methods=True)
    p1.fazer_aniversario()
    p1.dar_aula()

    f1 = Funcionario('Claudia', 27, 'Coordenadora', 'Administrativo')
    f1.fazer_aniversario()
    f1.bater_ponto()

if __name__ == '__main__':
    main()