nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:=^20}!'.format(nome))

# : - Indica que o que segue são especificações de formatação.
# = - É o caractere que será usado para preencher o espaço ao redor do texto centralizado. Esse caractere é escolhido arbitrariamente e pode ser qualquer outro caractere se você quer preencher com algo diferente de espaços ou outro caractere padrão.
# ^ - Especifica que o texto deve ser centralizado dentro do espaço dado.
# 20 - Define a largura total do campo no qual o texto vai ser centralizado.
# Portanto, {:=^20} significa: "Substitua aqui com o texto fornecido (nome), centralize esse texto em um campo de 20 caracteres de largura, e use o símbolo = para preencher os espaços restantes à esquerda e à direita do texto centralizado".
