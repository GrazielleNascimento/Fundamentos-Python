salario = float(input('Informe seu salario: '))


if(salario > 1250):
    salario_a = salario + (salario * 0.10)
    print(f'seu novo salario é {salario_a:.2f}')
else:
    salario_b = salario + (salario * 0.15)
    print(f'Seu novo salario é {salario_b:.2f}')
