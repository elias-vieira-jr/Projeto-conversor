with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.readlines()

nconteudo = []
for linha in conteudo:
    nconteudo.append(linha.replace('Python', 'PYTHON'))

print(nconteudo)
texto = ''.join(nconteudo)

with open('texto2.txt', 'w') as arquivo:
    arquivo.write(texto)
