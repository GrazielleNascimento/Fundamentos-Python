# Definição da classe Bicicleta
class Bicicleta:
    def __init__(self, cor: str, modelo: str, ano: int, valor: float):
        # O método construtor inicializa o objeto com os atributos fornecidos
        # e realiza a conversão de tipo conforme necessário
        self.cor = cor            # Atributo para armazenar a cor da bicicleta
        self.modelo = modelo      # Atributo para armazenar o modelo da bicicleta
        self.ano = int(ano)       # Atributo para armazenar o ano (convertido para inteiro)
        self.valor = float(valor) # Atributo para armazenar o valor (convertido para float)
        
    # Método para simular o som da buzina da bicicleta
    def buzinar(self):
        print("Buzina!!!")

    # Método para simular a parada da bicicleta
    def parar(self):
        print("Parar!")

    # Método para simular a corrida da bicicleta
    def correr(self):
        print("Correndo!")
    

    # Método mágico __str__ usado para representar o objeto como uma string
    def __str__(self):
        # Retorna uma descrição formatada do objeto Bicicleta
        return (f'Bicicleta(cor={self.cor}, modelo={self.modelo}, '
                f'ano={self.ano}, valor=R${self.valor:.2f})')

# Criando uma instância da classe Bicicleta com os dados fornecidos
minha_bicicleta = Bicicleta("rosa", "neon", 2000, 1200.00)

# Imprimindo a representação da instância minha_bicicleta
print(minha_bicicleta)

print(minha_bicicleta.cor)
# Chamando métodos da instância minha_bicicleta
minha_bicicleta.correr()
minha_bicicleta.buzinar()
minha_bicicleta.parar()

# Exibindo os detalhes da bicicleta através da interpolação de strings
# com formatação de valor monetário para o atributo valor
print(f'A minha bicicleta possui a cor {minha_bicicleta.cor}, '
      f'modelo {minha_bicicleta.modelo}, ano {minha_bicicleta.ano} '
      f'e valor R${minha_bicicleta.valor:.2f}.')
