with open('texto.txt', 'r') as arquivo:
    conteudo = arquivo.read()

with open('copia.txt', 'w') as arquivo:
    arquivo.write(conteudo)