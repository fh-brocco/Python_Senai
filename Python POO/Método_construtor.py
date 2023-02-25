class Pessoa: #Classe principal
    def __init__(self, nome, sexo, cpf, dataNascimento, email, ativo): #Método construtor da classe
        self.nome = nome #self indica uma referência para o objeto    
        self.sexo = sexo
        self.cpf = cpf
        self.dataNascimento = dataNascimento
        self.email = email
        self.ativo = ativo
    def desativar(self):
        self.ativo = False
        print('A pessoa foi desativada com sucesso')

if __name__ == "__main__":
    pessoa1 = Pessoa('Fernando','Masculino','123.456.789-00','01/01/2023','fernando@brocco.com',True)
    pessoa1.desativar()