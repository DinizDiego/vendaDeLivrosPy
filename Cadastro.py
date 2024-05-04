class Cadastro:
    # Construtor
    def __init__(self):
        self.nome = []
        self.endereco = []
        self.telefone = []
        self.dtNascimento = []
        self.login = []
        self.senha = []

    def cadastrar(self, nome, endereco, telefone, dia, mes, ano, login, senha):
        self.nome.append(nome)
        self.endereco.append(endereco)
        self.telefone.append(telefone)
        self.dtNascimento.append(f"{dia}/{mes}/{ano}")
        self.login.append(login)
        self.senha.append(senha)

        return "Cadastrado!"

    def validacaoLogin(self, login, senha):
        self.login = login
        self.senha = senha
        if(login != self.login or senha != self.senha):
            print("Erro! Login ou senha inválido(s).\n")
        else:
            print("Logado com sucesso!")


