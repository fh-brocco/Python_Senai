import shutil
import os

origem = 'C:/Users/Aluno/Documents/Brocco/Origem' #caminho pasta de origem
destino = 'C:/Users/Aluno/Documents/Brocco/Destino' #caminho pasta de destino
extensao = '.jpg' #extensões de arquivos de preferência

for nomearquivo in os.listdir(origem):
    if nomearquivo.endswith(extensao):
            shutil.copy(os.path.join(origem, nomearquivo), (os.path.join(destino, nomearquivo)))
