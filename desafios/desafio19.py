# Crie a classe Livro, que vai simular a passagem de páginas de um livro
# Considerando também se o usuário chegou ao fim da leitura
from rich import print

class Livro:
    def __init__(self, nome, paginas):
        self.nome = nome
        self.paginas = paginas
        self.paginaAtual = 1

        print(f"Você acabou de abrir o livro {self.nome} que tem {self.paginas} e está na pág {self.paginaAtual}")


    def passarPaginas(self, qnt = 1):
        contador = 0

        for pag in range(0, qnt, 1):
            if not self.fimLivro():
                print(f"\rPág{pag} :arrow_forward: ", end="")
                self.paginaAtual += 1
                contador+=1                    
        print(f" Você avançou {qnt} páginas do seu livro e está na {self.paginaAtual}")
        if self.fimLivro():
            print("Você chegou ao fim do livro.")

    def fimLivro(self) -> bool:
        if self.paginaAtual == self.paginas:
            return True
        return False

l1 = Livro('Pequeno Príncipe', 20)
l1.passarPaginas(21)
l1.passarPaginas(3)
