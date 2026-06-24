from ex010 import Avaliacao
from rich import print, inspect
def main():
    av1 = Avaliacao('Carlos', 'Matemática', 9.5)
    inspect(av1, private=True)

    av1.nota = 3.5
 
if __name__ == '__main__':
    main()