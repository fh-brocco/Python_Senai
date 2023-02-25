class Pessoa: #Classe principal
    def __init__(self, nome, sobrenome,idade):
        self.nome = nome 
        self.sobrenome = sobrenome
        self.idade = idade
      
    def nome_completo(self):
       return f'{self.nome} {self.sobrenome}'
    
class PessoaAutenticavel(Pessoa): #classe filha
    def __init__(self, nome, sobrenome, idade, usuario, senha):
        Pessoa.__init__(self, nome, sobrenome, idade)
        self.usuario = usuario
        self.senha = senha

    def autenticar(self, usuario, senha):
        return self.usuario == usuario and self.senha == senha

p = PessoaAutenticavel('Fernando','Brocco',31,'brocco','minhasenha123')

print(Pessoa.nome_completo(p))
print(PessoaAutenticavel.autenticar(p,'brocco','minhasenha123')) 