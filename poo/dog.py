class Cachorro:
    # Método construtor que é chamado quando um novo objeto Cachorro é criado.
    def __init__(self, nome, cor, acordado=True):
        # Atributos de instância inicializados com os valores passados nos parâmetros.
        self.nome = nome  # Nome do cachorro.
        self.cor = cor  # Cor do cachorro.
        self.acordado = acordado  # Estado do cachorro. True para acordado, False para dormindo. Padrão é True.

    # Método para o cachorro latir.
    def latir(self):
        print('Auau')  # Ação de latir, exibe uma mensagem no console.

    # Método para fazer o cachorro dormir.
    def dormir(self):
        self.acordado = False  # Altera o estado para falso indicando que o cachorro está dormindo.
        print("Zzzzz...")  # Simula o som do cachorro dormindo.

# Criando uma instância da classe Cachorro com o nome 'chappie', cor 'amarelo' e estado inicial dormindo (False).
cao_1 = Cachorro('chappie', 'amarelo', False)
# Criando outra instância da classe Cachorro com o nome 'Aladim', cor 'branco e preto'.
# O estado inicial acordado(True) é o padrão, então não precisa ser passado.
cao_2 = Cachorro('Aladim', 'branco e preto')

# Usando o método latir() na primeira instância do cachorro. Isso vai imprimir "Auau" no console.
cao_1.latir()

# Imprimindo o estado atual do segundo cachorro (True se estiver acordado).
print(cao_2.acordado)
# Chamando o método dormir() para fazer o segundo cachorro dormir.
# Isso vai alterar o estado para False e imprimir "Zzzzz..." no console.
cao_2.dormir()
# Imprimindo o estado do segundo cachorro após chamar dormir(). Agora deve ser False.
print(cao_2.acordado)
