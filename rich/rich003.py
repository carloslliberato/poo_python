from rich import print
from rich.table import Table

tabela = Table(title="Tabela de Preços")

tabela.add_column('Nome')
tabela.add_column('Preço')
tabela.add_row('Lápis', 'R$1,00')
tabela.add_row('Caderno', 'R$15,00')

print(tabela)