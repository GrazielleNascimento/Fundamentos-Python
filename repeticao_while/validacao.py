
p
sexo = str(input('Informe seu sexo [M/F]: ')).upper()[0].strip()
while sexo not in 'MmFf':
  sexo = str(input('Dados invalidos. digite o sexo: ')).upper()[0].strip()
print(f'Sexo {sexo} registrado com sucesso!')
# if(sexo != 'M' or sexo != 'F'):
