distancia = float(input('Digite a distancia em KM: '))
tipoa = (distancia * 0.50)
tipob = (distancia * 0.45)
if( distancia <= 200):
    print(f'O valor da sua viagem é {tipoa:.2f} do tipo A')
else:
    print(f'O valor da sua viagem é {tipob:.2f}  do tipo B')

