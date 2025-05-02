with open('copia.txt', 'r') as arquivo:
    conteudo = arquivo.read()

print('-'*90)
print(conteudo)
print('-'*90)

frase = str(input('Qual frase deseja adicionar ao texto? '))

with open('copia.txt', 'a') as arquivo:
    arquivo.write(frase + '\n')