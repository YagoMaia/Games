from random import randint
from time import sleep
nome = str(input('Digite seu nome: ')).strip().title()
ataque_inimigo = randint(20, 30)
ataque_heroi = randint(20, 30)
vida_heroi = 100
vida_inimigo = 100
while True:
    print('''Vida de {}: {}
Vida do Inimigo: {}'''.format(nome, vida_heroi, vida_inimigo))
    sleep(1)
    print('Seu turno:')
    sleep(1)
    print('Você atacou e causou {} de dano'.format(ataque_heroi))
    vida_inimigo = vida_inimigo - ataque_heroi
    if vida_inimigo <= 0:
        break
    ataque_heroi = randint(20, 30)
    sleep(1)
    print('Turno do inimigo')
    sleep(1)
    print('O inimigo atacou e causou {} de dano'.format(ataque_inimigo))
    vida_heroi = vida_heroi - ataque_inimigo
    if vida_heroi <= 0:
        break
    ataque_inimigo = randint(20, 30)
    sleep(1)
print('A luta acabou')
sleep(1)
if vida_heroi <= 0:
    print('O inimigo ganhou!')
elif vida_inimigo <=0:
    print('Você ganhou!')

