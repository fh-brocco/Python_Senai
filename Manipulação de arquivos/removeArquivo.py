import os

diretorio = 'C:/Users/Aluno/Documents/Brocco/Destino' #caminho pasta de destino
extensao = '.jpg' #extensões de arquivos de preferência

for nomearquivo in os.listdir(diretorio): 
    if nomearquivo.endswith(extensao):
            os.remove(os.path.join(diretorio, nomearquivo)) #remoção de arquivos