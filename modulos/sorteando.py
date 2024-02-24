# Importa a função choice da biblioteca random.
import random 


# Imprime uma linha de asteriscos seguida da palavra "Randomly" e mais asteriscos.
print(f'{"*" * 25}Randomly{"*" * 25}')

# Solicita ao usuário para inserir o nome do primeiro estudante e armazena na variável first_student.
first_student = str(input('Enter the first student: '))
# Solicita ao usuário para inserir o nome do segundo estudante e armazena na variável second_student.
second_student = str(input('Enter the second student: '))
# Solicita ao usuário para inserir o nome do terceiro estudante e armazena na variável third_student.
third_student = str(input('Enter the third student: '))
# Solicita ao usuário para inserir o nome do quarto estudante e armazena na variável fourth_student.
fourth_student = str(input('Enter the fourth student:  '))

# Cria uma lista chamada 'students' contendo os nomes dos estudantes inseridos anteriormente.
students = [first_student, second_student, third_student, fourth_student]
# Utiliza a função random.choice para seleção aleatória de um item da lista 'students'.
chosen = random.choice(students)

# Imprime o nome do estudante escolhido aleatoriamente, formatado dentro de uma frase.
print(f'\nThe chosen student was {chosen}')
