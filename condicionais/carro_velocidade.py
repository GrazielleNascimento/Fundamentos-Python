velocidade = float(input('Informe a velocidade do carro: '))
multa = (velocidade - 80) * 7
if velocidade > 80:
    print('\33[1;31mCarro Multado')
    print('A multa vai custar 7.00 por cada km acima do limite')
    print(f'A multa vai custar: {multa}')
else:
    print('Tenha um Bom dia, dirija com segurança!')
   
    
      
