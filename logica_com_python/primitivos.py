nome = input('Digite algo: ')
print('O tipo primitivo desse valor é: ',type(nome))
print('Só tem espaços? ', nome.isspace())
print('é um numero? ', nome.isnumeric())
print('é alfabetico? ', nome.isalpha())
print('é alfanumerico? ', nome.isalnum())
print('esta em maiusculas? ', nome.isupper())
print('esta em minusculas? ', nome.islower() )
print('esta capitalizada? ', nome.istitle())
