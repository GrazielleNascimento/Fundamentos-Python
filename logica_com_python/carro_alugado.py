dias_alugado = int(input('Quantos dias alugados? '))
km_rodados = float(input('Quantos Km Rodados? '))


pago = (dias_alugado * 60) + (km_rodados * 0.15)


print(f'O Total a pagar é de {pago:.2f}')
