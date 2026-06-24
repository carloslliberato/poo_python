from desafio28 import Termostato
from rich import inspect, print

t = Termostato()
inspect(t, methods=True, private=True)
t.temperatura = 25
inspect(t, methods=True, private=True)
print(t.ftemperatura)