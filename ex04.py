with open('texto.txt', 'r') as arquivo:
    texto = arquivo.read().upper()

palavra = str(input('Procure uma palavra no texto: ').upper())
total = texto.count(palavra)

print('-'*90)

if palavra in texto:
    print('Essa palavra existe no texto!')
    if total > 1:
        print(f'Ela aparece {total} vezes.')
    else:
        print(f'Ela aparece {total} vez.')
else:
    print('Essa palavra não existe no texto.')