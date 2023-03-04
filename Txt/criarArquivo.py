arquivo = open('texto.txt', '+') #Cria um arquivo na pasta de origem (nome do arquivo + extensão desejada entre as aspas)

arquivo.write('Manipulando arquivos \n') #Escreve dentro do arquivo criado

varios = list()
varios.append('\nbrincando \n')
varios.append('com manipulação \n')
varios.append('de arquivos \n')
varios.append('usando Python \n')

arquivo.writelines(varios)