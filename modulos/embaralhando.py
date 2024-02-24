# Importa a função shuffle do módulo random para embaralhar listas.
from random import shuffle 

# Solicita ao usuário para inserir o nome do primeiro estudante e armazena como uma string.
student1= str(input('Enter the first student: '))

# Solicita ao usuário para inserir o nome do segundo estudante e armazena como uma string.
student2= str(input('Enter the second student: '))

# Solicita ao usuário para inserir o nome do terceiro estudante e armazena como uma string.
student3= str(input('Enter the third student: '))

# Solicita ao usuário para inserir o nome do quarto estudante e armazena como uma string.
student4 = str(input('Enter the fourth student: '))

# Cria uma lista de estudantes com os nomes inseridos anteriormente.
students = [student1, student2, student3, student4]

# Embaralha a lista de estudantes. Note que shuffle não retorna um valor,
# a alteração é feita na própria lista passada como argumento.
chosed = shuffle(students) 

# Imprime a ordem dos estudantes para apresentação após o embaralhamento.
# Aqui podemos ver que a ordem dos elementos na lista 'students' foi alterada.
print(f'The students order to apresentation is: {students}')
