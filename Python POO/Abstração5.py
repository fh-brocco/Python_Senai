from Abstração4 import*
from Abstração2 import*
from Abstração3 import*

l =  Lancamento ('CREED 3', 10)
print ('Diária: R$ {:.2f}'.format(l.r_diaria()))

n = Comum ('Avatar 2', 7)
print('Diária: R$ {:.2f}'.format(n.r_diaria()))

i = Infantil ('Patas em Furia', 5)
print('Diária: R$ {:.2f}'.format(i.r_diaria()))

