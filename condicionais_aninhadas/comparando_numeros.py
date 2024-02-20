num1 = int(input('Informe o primeiro numero: '))
num2 = int(input('Informe o segundo numero: '))

if(num1 > num2):
    print(f'O numero {num1} é maior que o numero {num2}')
elif(num2 > num1):
    print(f'O {num2} é maior que {num1}')
else:
    print('Valores iguais')
