with open('arquivo1.txt', 'w') as file1, open('arquivo2.txt', 'w') as file2:
    file1.write('arquivo1.')
    file2.write('arquivo2.')

with open('arquivo1.txt', 'r') as file1, open('arquivo2.txt', 'r') as file2:
    conteudo1 = file1.read()
    conteudo2 = file2.read()

conteudo3 = conteudo1 + conteudo2

with open('arquivo3.txt', 'w') as file3:
    file3.write(conteudo3)
print(conteudo3)

#aqui da pra criar outro with open('arquivo.txt','r') as file3 e ler o resultado
# mas não fica otimizado

#Tambem daria pra fazer só um with open('arquivo3.txt','w+'), pq ai 
#ja fazia o file.write e o file.read
 
