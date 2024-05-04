from Cadastro import Cadastro
from Reserva import Reserva

class Control:
    # Constructor
    def __init__(self):
        self.cadas= Cadastro()
        self.reser = Reserva()
        self.opcao = -1

    def menu(self):
        self.opcao = int(input("\n***Bem Vindo à nossa loja de livros!*** \n\n" +
                               "\nÉ sua primeira vez aqui?" +
                               "\n0. Sair" +
                               "\n1. Sim" +
                               "\n2. Não"))

    def menuU(self):
        while(self.opcao != 0):
            print("Obrigado!Volte sempre.")
            if(self.opcao == 1):
            print("\n***CADASTRO*** \n\n")
