with open('arquivo1.txt', 'w') as file1:
    file1.write('arquivo1.\n')
    file1.write('Isso é um teste do desafio 3 do curso de Python.\n')
    file1.write('Vamos ver se conseguimos ler o conteúdo depois.\n')
    file1.write('O objetivo é escrevermos uma palavra no terminal e verficar se ela existe no arquivo.\n')
    file1.write('Se a palavra, existir, tem também que mostrar a linha dela no arquivo.\n')

with open('arquivo1.txt', 'r') as file1:
    conteudo1 = file1.read().splitlines()

palavra = str(input('Digite a palavra que deseja procurar no arquivo: '))

encontrado = False

for linha in conteudo1:
    if palavra in linha:
        print(f'A palavra "{palavra}" existe no arquivo e está na linha: {linha}')
        encontrado = True

if not encontrado:
    print(f'A palavra "{palavra}" não existe no arquivo.') 