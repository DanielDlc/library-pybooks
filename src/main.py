from interface import Interface
from livraria import Livraria

if __name__ == '__main__':
    # Inicializa a livraria e carrega os dados existentes
    minha_livraria = Livraria()
    minha_livraria.carregar_dados()

    # Inicia a interface gráfica
    interface = Interface(minha_livraria)
    interface.iniciar()

    # Salva os dados da livraria ao fechar o programa
    minha_livraria.salvar_dados()
