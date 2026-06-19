# Declaração de Classe
class Pessoa:
    """
    Essa classe cria uma pessoa que tem nome e idade

    Para criar uma nova pessoa, use
    variavel = Pessoa(nome, idade)
    """
    def __init__(self, nome='', idade=0): # Método Construtor
        #Atributos de Instancia
        self.nome = nome
        self.idade = idade
    
    # Métodos de Instância
    def aniversario(self):
        self.idade += 1
    
    def __str__(self):
        return f"{self.nome} tem {self.idade} anos de idade."
    
    def __getstate__(self):
        return f"Estado: nome = {self.nome}, idade = {self.idade}"
    
# Declaracao de Objetos
p1 = Pessoa("Carlos", 19)
print(p1)

p2 = Pessoa('André', 16)

p3 = Pessoa()

print(p1.__doc__) # DUNDER ATTRIBUTE
print(p1.__dict__) # Attribute
print(p1.__getstate__()) # Method
print(p1.__class__)