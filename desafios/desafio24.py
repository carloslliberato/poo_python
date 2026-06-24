from abc import ABC, abstractmethod

class BebidaQuente:

    def preparar(self):
        print('--- Iniciando o Preparo ---')
        self.ferver_agua()
        self.misturar()
        self.servir()
        print('--- Bebida Pronta ---')

    def ferver_agua(self):
        print("- Fervendo a agua a 100°C")
    
    @abstractmethod
    def misturar(self):
        pass
    @abstractmethod
    def servir(self):
        pass

class Cafe(BebidaQuente):

    def misturar(self):
        print("- Passando água pressurizada pelo pó de café moído")
    
    def servir(self):
        print("- Servindo em xícara pequena")

class Cha(BebidaQuente):

    def misturar(self):
        print('- Mergulhando o sachê de ervas na água')

    def servir(self):
        print('- Servindo na caneca de porcelana com limão')

class Leite(BebidaQuente):

    def misturar(self):
        print("- Passando vapor pressurizado pelo bico do leite")
    
    def servir(self):
        print("- Servir na caneca grande, já com café")
