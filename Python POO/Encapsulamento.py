class Pessoa:
    def __init__(self, nome, idade, cpf):
        self._nome = nome
        self. _idade = idade
        self._cpf = cpf

ps = Pessoa('Brocco', 31, '123.456.789-00')
print(ps._nome)
print(ps._idade)
print(ps._cpf)
