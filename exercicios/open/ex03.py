conteudo = 'A linguagem Python é uma das mais populares do mundo, utilizada em diversas áreas como desenvolvimento web, análise de dados, automação e inteligência artificial.\nSua sintaxe simplese legível facilita o aprendizado, mesmo para quem está começando na programação.\n'
with open('texto.txt', 'w') as arquivo:
    arquivo.write(conteudo)

with open('texto.txt', 'r') as arquivo:
    linhas = arquivo.readlines()
    texto = ''.join(linhas)

qtd_linhas = len(linhas)
palavras = texto.split()
qtd_palavras = len(palavras)

print('-'*90)
print(texto)
print()
print(f'Total de linhas: {qtd_linhas}')
print(f'Total de palavras: {qtd_palavras}')
