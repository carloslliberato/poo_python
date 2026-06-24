from ex009 import Avaliacao
from rich import print, inspect
def main():
    av1 = Avaliacao('Carlos', 'Matemática', 9.5)
    inspect(av1, private=True)

    av1.set_nota(6)
    inspect(av1, private=True)
 
if __name__ == '__main__':
    main()