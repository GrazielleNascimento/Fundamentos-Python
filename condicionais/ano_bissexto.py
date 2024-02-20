ano = int(input('Digite o ano que deseja consultar: '))

if(ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0):
    print(f'O Ano de {ano} é bissexto')
else:
    print(f'O Ano de {ano} não é bissexto')
