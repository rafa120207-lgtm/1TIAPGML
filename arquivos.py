with open('arquivo.txt','w') as file:
    file.write('Olá, mundo!')

with open('arquivo.txt','r+') as file:
    conteudo = file.read()
    file.write('\nAdicionando mais conteúdo.')  

with open('arquivo.txt','a') as file:
    file.write('\nMais uma linha no final do arquivo.')

with open('arquivo.txt','w') as file:
    file.write('Linha 1\n')
    file.write('Linha 2\n')
    file.write('Linha 3\n')