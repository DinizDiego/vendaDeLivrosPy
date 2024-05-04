class Reserva:
    # Construtor
    def __init__(self):
        # Construtor
        self.email = ['']
        self.opcao = -1

    def menuReserva(self):
        self.opcao = int(input("Livro indisponível!\n\n" +
                               "Deseja realizar a reserva?\n" +
                               "\n0. Sair" +
                               "\n1. Sim" +
                               "\n2. Não" +
                               "\nEscolha uma das opções acima:"))

    def menuR(self, email):
        while(self.opcao != 0):
            self.menuReserva()
            if(self.opcao == 1):
                self.email = email
                print("Digite seu email para contato: ")

                print("\nEnviaremos um email para " + email + " quando o livro estiver disponível!\n")
            elif(self.opcao == 2):
                print("Retornando para o Menu")
            else:
                print("A opção selecionada não é válida!")