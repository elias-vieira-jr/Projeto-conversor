dados = ['Nome: Elias Júnior', 'Idade: 21 anos', 'Cidade: Rondonópolis']
print(dados)

with open("dados.txt", "w") as arquivo:
    arquivo.write('\n'.join(dados))