#Exercicio 1
contador_palavras = 0
with open('arquivo.txt', 'w') as file:
    file.write('Olá, este é um arquivo de exemplo.')

with open('arquivo.txt', 'r') as file:
    for palavras in file.read().split():
        contador_palavras += 1

print(f'O número de palavras no arquivo é: {contador_palavras}')
#Fim ex01


