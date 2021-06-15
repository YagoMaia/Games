from time import sleep
from random import randint
# Introdução do RPG
jogadores = int(input('Quantas pessoas jogarão? '))

nome = str(input('Digite o nome do seu personagem: ')).strip().lower().title()
classes = ('Paladino', 'Mago', 'Arqueiro', 'Necromante', 'Escudeiro' )
raça = ('Elfo', 'Humano', 'Orc', 'Morto-Vivo', 'Anão')
print(''' \033[1;32mElfo:\033[m É uma raça que predomina sua inteligência;
Muito boas com armas de longa distância
 \033[1;33mHumano:\033[m Raça que predomina sua imbecialidade
Muito boa com armas de curta distância
 \033[1;34mOrc:\033[m Raça que predomina a força física
Muito boa com arma de Grande porte
 \033[1;35mMorto-Vivo:\033[m Raça que está parcialmete viva
Muito boa com magias
 \033[1;36mAnão:\033[m Raça com pouca altura
Muito bons para fazer armas e armadilhas''')
escolha_raça = int(input('''As opções são:
[ 1 ] - Elfo
[ 2 ] - Humano
[ 3 ] - Orc
[ 4 ] - Morto-Vivo
[ 5 ] - Anão
Qual será sua raça? '''))
escolha_classe = int(input('''As opções são:
[ 1 ] - Paladino
[ 2 ] - Mago
[ 3 ] - Arqueiro
[ 4 ] - Necromante
[ 5 ] - Escudeiro
Qual será sua classe? '''))
print('-=-' * 10)
print('Nome: {}'.format(nome))
print('Raça: {}'.format(raça[escolha_raça - 1]))
print('Classe: {}'.format(classes[escolha_classe - 1]))
print('Level : 1')
print('-=-' * 10)



