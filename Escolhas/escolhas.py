from time import sleep
from random import randint
import pygame
pygame.init()
pygame.mixer.music.load('inicio.mp3')
pygame.mixer.music.play()
# Não vai dá pra fazer do jeito que eu quero, uma vez que no pycharm trava muito...
fosf = 5
resp = 1
cont = 0
vida = 3
itens = []
print('\033[32mVocê acorda em um lugar escuro...')
sleep(3)
print('Está muito frio...')
sleep(3)
print('Tem apenas você, uma caixa de fosforo e uma lareira...')
sleep(3)
print('O que você fará? ')
sleep(1)
while resp == 1 and fosf > 0:
    resp = int(input('''\033[37m[ 1 ] - Usar o fosforo para acender a lareira
[ 2 ] - Se enconlher em um canto: \033[37m'''))
    if resp == 2:
        print('Sua opção não foi tão boa...')
        sleep(1)
        print('Você morreu de frio...')
    else:
        pygame.mixer.music.load('fosforo.mp3')
        pygame.mixer.music.play()
        sleep(2)
        acender = [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0]
        sorte = randint(0, 9)
        if fosf != 0:
            if acender[sorte] == 1:
                sleep(1)
                print('\033[33mVocê conseguiu acender a lareira\033[m')
                sleep(2)
                print('\033[32mO frio está se esvaindo ao pouco...')
                sleep(2)
                print('Agora que está mais quente você observa o quarto com mais precisão')
                sleep(2)
                print('Após observar bem, percebe que está em uma cabana com uma vista para um floresta...')
                sleep(2)
                pygame.mixer.music.load('inicio.mp3')
                pygame.mixer.music.play()
                while resp != 3:
                    resp = int(input('''\033[37m[ 1 ] - Observar pela janela
[ 2 ] - Explorar a cabana
[ 3 ] - Sair da cabana: \033[37m'''))
                    if resp == 1:
                        if cont == 0:
                            print('\033[32mVocê consegue observar poucas coisas...')
                            sleep(2)
                            print('Você acaba de ver um vulto...')
                            sleep(2)
                            print('* Você se afasta da janela *')
                            cont += 1
                        else:
                            sleep(2)
                            print('\033[32mAs coisas continuam como antes...')
                            sleep(2)
                            print('Mas o vulto não está mais lá...')
                            sleep(2)
                    elif resp == 2:
                        sleep(2)
                        print('\033[32mVocê explora a cabana...')
                        sleep(2)
                        print('Após explorar a cabana você conseguiu uma lanterna')
                        sleep(2)
                        print('Iten obtido: Lanterna')
                        itens += ['Lanterna']
                        sleep(2)
                    elif resp == 3:
                        sleep(2)
                        print('\033[32mVocê sai da cabana para explorar...')
                        if len(itens) == 0:
                            sleep(2)
                            print('Está muito escuro...')
                            sleep(2)
                            print('Você escuta uns sons...')
                            sleep(2)
                            print('Pela falta de luminisidade você pisa em uma armadilha')
                            sleep(2)
                            print('* Sua perna está presa e você está morrendo de dor *')
                            while vida != 0:
                                tirar = [0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 0]
                                sorte = randint(0, 9)
                                if tirar[sorte] == 0:
                                    if vida == 3:
                                        sleep(2)
                                        print('Você tenta tirar a perna, mas não consegue')
                                        sleep(2)
                                        print('* Você parece tonto *')
                                        vida -= 1
                                        sorte = randint(0, 9)
                                    elif vida == 2:
                                        sleep(2)
                                        print('Você tenta NOVAMENTE tirar a perna, mas não consegue')
                                        sleep(2)
                                        print('* Sua visão parece turva... *')
                                        vida -= 1
                                        sorte = randint(0, 9)
                                    elif vida == 1:
                                        sleep(2)
                                        print('Você está sem forças, não consegue tirar a perna')
                                        sleep(2)
                                        print('* Você está prestes a desmaiar *')
                                        vida -= 1
                                        sorte = randint(0, 9)
                                else:
                                    sleep(2)
                                    print('Você conseguiu tirar a armadilha do seu pé...')
                                    sleep(2)
                                    print('* Sua perna está sangrando *')
                                    break
                        else:
                            sleep(2)
                            print('* Lanterna é acessa *')
                            sleep(2)
                            print('Você consegue ver com mais clareza...')
                            sleep(2)
                            print('Observa-se arvorés, corujas, uma armadilha no chão...')
                            sleep(2)
                            print('* Você evita a armadilha *')
                            sleep(2)
                            print('* Barulho de galho quebrando *')
                            pygame.mixer.music.load('galho.mp3')
                            pygame.mixer.music.play()
                            sleep(2)
                            print('O que você fará?')

            else:
                sleep(2)
                print('\033[31mO fosforo não acendeu...\033[m')
                sleep(2)
                fosf -= 1
                print(f'\033[32mFaltam {fosf} fosforos...')
                sleep(2)
    if fosf == 0:
        sleep(2)
        print('\033[32mSua sorte não foi tão boa...')
        sleep(2)
        print('Você morreu de frio...')
