from math import radians, sin, cos, tan

angulo = float(input('Digite o angulo que voce deseja: '))
angulo_em_radianos = radians(angulo)
seno = sin(angulo_em_radianos)
cosseno = cos(angulo_em_radianos)
tangente = tan(angulo_em_radianos)

print(f'O angulo de {angulo} tem o SENO de {seno:.2f}')
print(f'O angulo de {angulo} tem o COSSENO de {cosseno:.2f}')
print(f'O angulo de {angulo} tem a Tangentede {tangente:.2f}')
