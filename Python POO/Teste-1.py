class Pessoa: #Classe principal
    def __init__(self, nome, sexo, cpf,dataNascimento,email): #Método construtor da classe
        self.nome = nome #self indica uma referência para o objeto    
        self.sexo = sexo
        self.cpf = cpf
        
    def soma(self):
        #total = self.x*self.x*self.x
        total = self.x+self.y
        return 'Soma realizada: ' + str(total)
    
calc = Teste(800) 
c =  calc.soma() #instanciando um objeto
print(c)