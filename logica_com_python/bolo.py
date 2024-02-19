class bolo:
    def __init__(self, sabor, cobertura, valor):
        self.sabor = sabor
        self. cobertura = cobertura
        self.valor= valor
        
meu_bolo = bolo(sabor ='chocolate', cobertura='coco', valor='50')

print('meu bolo de', meu_bolo.sabor, 'com a cobertura de', meu_bolo.cobertura, 'no valor de', meu_bolo.valor, 'reais')
