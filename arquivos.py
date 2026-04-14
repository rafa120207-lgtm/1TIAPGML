with open('arquivo.txt','w') as file:
    file.write('Olá, mundo!')

with open('arquivo.txt','r+') as file:
    conteudo = file.read()
    file.write('\nAdicionando mais conteúdo.')  

with open('arquivo.txt','a') as file:
    file.write('\nMais uma linha no final do arquivo.')