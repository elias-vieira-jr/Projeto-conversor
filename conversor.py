import csv

with open('original.txt', newline='', encoding='latin-1') as arquivo:
    conteudo_arquivo = csv.reader(arquivo, skipinitialspace=True)

    topo = '|0000|32787933000167|'
    linha_6000 = '|6000|X||||'

    conteudo_formatado = []

    conteudo_formatado.append(topo)

    for linha in conteudo_arquivo:
        data = linha[0]
        debito = linha[1]
        credito = linha[2]
        descricao = linha[3].strip()
        valor = linha[4].lstrip('0').replace('.', ',')
        usuario = "ELIAS.VIEIRA"
        empresa = "103"

        conteudo_formatado.append(linha_6000)
        conteudo_formatado.append(f'|6100|{data}|{debito}|{credito}|{valor}||{descricao}|{usuario}|{empresa}|||')

with open('saida.txt', 'w') as saida:
    for linha in conteudo_formatado:
        saida.write(linha + '\n')
