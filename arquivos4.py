with open('arquivo1.txt', 'w') as file1:
    file1.write('Teste do desafio 4 do curso de Python.\n')
    file1.write('O desafio é ler o arquivo\n')
    file1.write('z, E ordenar as linhas em ordem alfabética\n')
    file1.write('Depois escrever o resultado em um novo arquivo\n')

with open('arquivo1.txt', 'r') as file1:
    conteudo1 = file1.read().splitlines()
conteudo1.sort()

with open('arquivo_ordenado.txt', 'w') as file2:
    for linha in conteudo1:
        file2.write(linha + '\n')

with open('arquivo_ordenado.txt', 'r') as file2:
    conteudo_ordenado = file2.read()
print(conteudo_ordenado)