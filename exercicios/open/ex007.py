with open('arquivo_ex07.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()

print(conteudo)
print('-'*90)

nconteudo = [linha for linha in conteudo if linha.strip() != '']

print(nconteudo)