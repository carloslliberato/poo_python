# Declaração de Classe
class Pessoa:
    def __init__(self): # Método Construtor
        #Atributos de Instancia
        self.nome = ''
        self.idade = 0
    
    # Métodos de Instância
    def aniversario(self):
        self.idade += 1

    def mensagem(self):
        return f"{self.nome} tem {self.idade} anos de idade."
    
# Declaracao de Objetos
p1 = Pessoa()
p1.nome = 'Carlos'
p1.idade = 19
print(p1.mensagem())
p1.aniversario()
print(p1.mensagem())
"""
A chamada fica assim:
    print(p1.mensagem())
    self.nome -> p1.nome
        Carlos
"""

p2 = Pessoa()
p2.nome = 'André'
p2.idade =  16
print(p2.mensagem())