from src.interface_usuario import Interface
from src.livraria import Livraria

if __name__ == '__main__':
    minha_livraria = Livraria()
    minha_livraria.carregar_dados()

    interface = Interface(minha_livraria)
    interface.iniciar()

    minha_livraria.salvar_dados()