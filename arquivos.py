with open('meuarquivo.txt', 'w') as file:
    file.write('Olá, mundo!\n')
    file.write('Este é um arquivo de texto.\n')
    file.write('Criado por Rafael\n')

with open('meuarquivo.txt', 'r') as file:
    conteudo = file.read()
    print(conteudo)
