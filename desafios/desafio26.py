from abc import ABC, abstractmethod

class Funcionario(ABC):
    sal_min = 1615
    inss = 7.5
    def __init__(self, nome = None):
        self.nome = nome
        self.salario_bruto = 0
        self.salario = 0


    @abstractmethod
    def calc_sal(self):
        pass

    def analisar_sal(self):
        corr = self.salario/Funcionario.sal_min
        return f'O salário corresponde a {corr:,.1f}'

class Horista(Funcionario):
    def __init__(self, nome, valor_hora=7.37, horas_trab=220):
        super().__init__(nome)
        self.nome = nome
        self.valor_hora = valor_hora
        self.horas_trab = horas_trab
        self.salario_bruto = self.valor_hora * self.horas_trab
    
    def calc_sal(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.inss/100)
        return f'R${self.salario:,.2f}'
    
class Mensalista(Funcionario):
    def __init__(self, nome, salario_bruto):
        super().__init__(nome)

        self.salario_bruto = salario_bruto

    def calc_sal(self):
        self.salario = self.salario_bruto - (self.salario_bruto * Funcionario.inss/100)
        return f'R${self.salario:,.2f}'
    

f1 = Horista('Carlos', 12, 190)
print(f1.calc_sal())
print(f1.analisar_sal())

f2 = Mensalista('Carlos', 2000)
print(f2.calc_sal())
print(f2.analisar_sal())