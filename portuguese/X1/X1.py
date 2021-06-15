from time import sleep
from random import randint
from math import ceil
print(f'{"Bem Vindo ao X1":=^30}')
classes = ['Arqueiro', 'Paladino', 'Mago', 'Assassino']
classes_jogadores = []
nomes = []
ações = []
cont1 = cont2 = rod = cont1_gelo = cont2_gelo = 1
status1 = '\033[1;37mNormal\033[m'
status2 = '\033[1;37mNormal\033[m'
jogador1 = hp1 = 500
jogador2 = hp2 = 500
crit = [0, 0, 0, 1, 0, 1, 1, 0, 0, 0]
ven = [0, 1, 0, 0, 1, 0, 0, 0, 0, 1]
fogo = [0, 1, 0, 0, 1, 0, 0, 0, 0, 1]
gelo = [0, 0, 1, 0, 0, 0, 1, 0, 1, 0]
for j in range(1, 3):
    nome = str(input(f'Digite o nome do jogador {j}: ')).strip().title()
    esc = int(input(f'''[ 1 ] - Arqueiro
[ 2 ] - Paladino
[ 3 ] - Mago
[ 4 ] - Assasino
Escolha a classe do jogador {j}: '''))
    print(f'A classe escolhida foi {classes[esc - 1]}')
    print('-=' * 18)
    classes_jogadores += [classes[esc - 1]]
    nomes += [nome]
Arqueiro = ['Flecha Perfurante', 'Flecha Envenenada',
            'Bomba de Fumaça', 'Chuva de Flechas',
            'Poção']
dano_arqueiro = [10, 20, 0, 45, 50]
Paladino = ['Investida', 'Escudo Divino',
            'Ira', 'Machadada', 'Poção']
dano_paladino = [10, 0, 0, 45, 50]
Mago = ['Bola de Fogo', 'Raio de Gelo',
        'Trovão', 'Jato de Água', 'Poção']
dano_mago = [10, 30, 40, 20, 50]
Assassino = ['Ataque Furtivo', 'Golpe Venenoso',
             'Apunhalada', 'Lançamento de Adaga',
             'Poção']
dano_assassino = [10, 20, 40, 10, 50]
for c in range(0, 2):
    if classes_jogadores[c] == 'Arqueiro':
        ação = (f'''[ 1 ] - {Arqueiro[0]}
[ 2 ] - {Arqueiro[1]}
[ 3 ] - {Arqueiro[2]}
[ 4 ] - {Arqueiro[3]}
[ 5 ] - {Arqueiro[4]}''')
        ações += [ação]
    if classes_jogadores[c] == 'Paladino':
        ação = (f'''[ 1 ] - {Paladino[0]}
[ 2 ] - {Paladino[1]}
[ 3 ] - {Paladino[2]}
[ 4 ] - {Paladino[3]}
[ 5 ] - {Paladino[4]}''')
        ações += [ação]
    if classes_jogadores[c] == 'Mago':
        ação = (f'''[ 1 ] - {Mago[0]}
[ 2 ] - {Mago[1]}
[ 3 ] - {Mago[2]}
[ 4 ] - {Mago[3]}
[ 5 ] - {Mago[4]}''')
        ações += [ação]
    if classes_jogadores[c] == 'Assassino':
        ação = (f'''[ 1 ] - {Assassino[0]}
[ 2 ] - {Assassino[1]}
[ 3 ] - {Assassino[2]}
[ 4 ] - {Assassino[3]}
[ 5 ] - {Assassino[4]}''')
        ações += [ação]
while True:
    print('-=' * 20)
    print(f'{"Rodada":>20} {rod:<20}')
    print('-=' * 20)
    sleep(1)
    if status1 != '\033[1;33mCongelado\033[m':
        if 550 >= hp1 > 250:
            print(f'{nomes[0]}: \033[1;32m{hp1}\033[m pontos de vida Status:{status1}')
        elif 250 >= hp1 > 135:
            print(f'{nomes[0]}: \033[1;33m{hp1}\033[m pontos de vida Status:{status1}')
        elif 135 >= hp1 > 0:
            print(f'{nomes[0]}: \033[1;31m{hp1}\033[m pontos de vida Status:{status1}')
        if 550 >= hp2 > 250:
            print(f'{nomes[1]}: \033[1;32m{hp2}\033[m pontos de vida Status:{status2}')
        elif 250 >= hp2 > 135:
            print(f'{nomes[1]}: \033[1;33m{hp2}\033[m pontos de vida Status:{status2}')
        elif 135 >= hp2 > 0:
            print(f'{nomes[1]}: \033[1;31m{hp2}\033[m pontos de vida Status:{status2}')
        print('=' * 37)
        print(f'Ataques disponiveis para o {nomes[0]}:')
        print(ações[0])
        ato1 = int(input('Qual será sua ação? ')) - 1
        sorte1 = randint(0, 9)
        if classes_jogadores[0] == 'Arqueiro':
            if ato1 != 4:
                crit1 = crit[sorte1]
                if crit1 == 1:
                    dano1 = dano_arqueiro[ato1] * 2
                    print('\033[1;31mCRITICO\033[m')
                else:
                    dano1 = dano_arqueiro[ato1]
            sleep(1)
            if ato1 != 4 and ato1 != 1:
                print(f'Habilidade usada: {Arqueiro[ato1]}')
                sleep(1)
                print(f'Dano causado: {dano1}')
            elif ato1 == 1:
                print(f'Habilidade usada: {Arqueiro[ato1]}')
                sleep(1)
                print(f'Dano causado: {dano1}')
                chance_ven1 = randint(0, 9)
                if ven[chance_ven1] == 1:
                    sleep(1)
                    print('\033[1;32mO inimigo ficou ENVENENADO\033[m')
                    sleep(1)
                    print('Causará um dano igual a 1% do Hp')
                    status2 = '\033[1;32mEnvenenado\033[m'
            elif ato1 == 4:
                print(f'Habilidade usada: {Arqueiro[ato1]}')
                sleep(1)
                print('Vida Recupurada: +150')
        elif classes_jogadores[0] == 'Paladino':
            dano1 = dano_paladino[ato1]
            sleep(1)
            if ato1 != 4 and ato1 != 1 and ato1 != 2:
                print(f'Habilidade usada: {Paladino[ato1]}')
                sleep(1)
                print(f'Dano causado: {dano1}')
            elif ato1 == 1:
                print(f'Habilidade usada: {Paladino[ato1]}')
                sleep(1)
                print(f'Dano Reduzido em 50%')
                status1 = '\033[1;35mProtegido\033[m'
            elif ato1 == 2:
                print(f'Habilidade usada: {Paladino[ato1]}')
                sleep(1)
                print(f'Ataque aumenta em 50%')
                status1 = '\033[1;31mPuto\033[m'
            elif ato1 == 4:
                print(f'Habilidade usada: {Paladino[ato1]}')
                sleep(1)
                print(f'Vida Recupurada: +150')
        elif classes_jogadores[0] == 'Mago':
            dano1 = dano_mago[ato1]
            sleep(1)
            if ato1 != 4 and ato1 != 0 and ato1 != 3 and ato1 != 2 and ato1 != 1:
                print(f'Habilidade usada: {Mago[ato1]}')
                sleep(1)
                print(f'Dano causado: {dano1}')
            elif ato1 == 0:
                print(f'Habilidade usada: {Mago[ato1]}')
                sleep(1)
                print(f'Dano causado: {dano1}')
                chance_fogo1 = randint(0, 9)
                if fogo[chance_fogo1] == 1:
                    if status2 != '\033[1;34mMolhado\033[m' and status2 != '\033[1;33mCongelado\033[m':
                        sleep(1)
                        print('\033[1;31mO inimigo está QUEIMANDO\033[m')
                        sleep(1)
                        print('Causará um dano redução de 30% do dano')
                        status2 = '\033[1;31mQueimando\033[m'
                    elif status2 == '\033[1;34mMolhado\033[m':
                        sleep(1)
                        print('O inimigo acabou de tomar uma sauna...')
                        status2 = '\033[1;37mNormal\033[m'
                    elif status2 == '\033[1;33mCongelado\033[m':
                        sleep(1)
                        print('O inimigo foi descongelado...')
                        status2 = '\033[1;37mNormal\033[m'
            elif ato1 == 3:
                print(f'Habilidade usada: {Mago[ato1]}')
                sleep(1)
                print(f'Dano causado: {dano1}')
                sleep(1)
                if status2 != '\033[1;31mQueimando\033[m':
                    print('O inimigo está MOLHADO')
                    status2 = '\033[1;34mMolhado\033[m'
                else:
                    print('O inimigo acabou de tomar banho...')
                    status2 = '\033[1;37mNormal\033[m'
            elif ato1 == 2:
                if status2 != '\033[1;34mMolhado\033[m':
                    print(f'Habilidade usada: {Mago[ato1]}')
                    sleep(1)
                    print(f'Dano causado: {dano1}')
                elif status2 == '\033[1;34mMolhado\033[m':
                    sleep(1)
                    print('\033[1;36mFoi realizado um ataque ELEMENTAL\033[m')
                    dano1 = dano1 * 2
                    sleep(1)
                    print(f'Habilidade usada: {Mago[ato1]}')
                    sleep(1)
                    print(f'Dano causado: {dano1}')
                    status2 = '\033[1;37mNormal\033[m'
            elif ato1 == 1:
                print(f'Habilidade usada: {Mago[ato1]}')
                sleep(1)
                print(f'Dano causado: {dano1}')
                chance_gelo1 = randint(0, 9)
                if gelo[chance_gelo1] == 1:
                    if status2 == '\033[1;31mQueimando\033[m':
                        sleep(1)
                        print('O inimigo sentiu uma leve brisa resfriante')
                        status2 = '\033[1;37mNormal\033[m'
                    else:
                        sleep(1)
                        print('\033[1;33mInimigo CONGELADO\033[m')
                        status2 = '\033[1;33mCongelado\033[m'
                        sleep(1)
                        if status2 != '\033[1;34mMolhado\033[m':
                            cont2_gelo = 1
                        else:
                            cont2_gelo = 0
            elif ato1 == 4:
                print(f'Habilidade usada: {Mago[ato1]}')
                sleep(1)
                print('Vida Recupurada: +150')
        elif classes_jogadores[0] == 'Assassino':
            dano1 = dano_assassino[ato1]
            sleep(1)
            if ato1 != 4 and ato1 != 1 and ato1 != 3:
                print(f'Habilidade usada: {Assassino[ato1]}')
                sleep(1)
                print(f'Dano causado: {dano1}')
            elif ato1 == 1:
                print(f'Habilidade usada: {Assassino[ato1]}')
                sleep(1)
                print(f'Dano causado: {dano1}')
                chance_ven1 = randint(0, 9)
                if ven[chance_ven1] == 1:
                    sleep(1)
                    print('\033[1;32mO inimigo ficou ENVENENADO\033[m')
                    sleep(1)
                    print('Causará um dano igual a 1% do Hp')
                    status2 = '\033[1;32mEnvenenado\033[m'
            elif ato1 == 3:
                sleep(1)
                print('Primeira adaga lançada...')
                adaga1 = randint(20, 40)
                sleep(1)
                print(f'Dano: {adaga1}')
                sleep(1)
                print('Segunda adaga lançada...')
                sleep(1)
                adaga2 = randint(20, 40)
                print(f'Dano: {adaga2}')
                sleep(1)
                dano1 = adaga1 + adaga2
                print(f'Dano total: {dano1}')
                sleep(1)
            elif ato1 == 4:
                print(f'Habilidade usada: {Assassino[ato1]}')
                sleep(1)
                print('Vida Recupurada: +150')
        print('=' * 37)
        if status2 == '\033[1;34mProtegido\033[m':
            hp2 -= ceil((dano1/2))
            cont2 += 1
            if cont2 == 3:
                print('\033[1;35mBUFF de defesa acabou\033[m')
                print('=' * 37)
                status2 = '\033[1;37mNormal\033[m'
        elif status2 == '\033[1;3mPuto\033[m':
            cont2 += 1
            if cont2 == 3:
                print('\033[1;35mVocê não está mais PUTO\033[m')
                print('=' * 37)
                status2 = '\033[1;37mNormal\033[m'
        elif status2 != '\033[1;3mPuto\033[m' or status2 != '\033[1;34mProtegido\033[m':
            if ato1 != 4:
                if status1 == '\033[1;37mNormal\033[m' or status1 == '\033[1;34mMolhado\033[m':
                    hp2 -= dano1
                elif status1 == '\033[1;31mPuto\033[m':
                    hp2 -= dano1 * 2
                if status2 == '\033[1;32mEnvenenado\033[m':
                    hp2 -= ceil(0.01*hp2)
                elif status1 == '\033[1;31mQueimando\033[m':
                    hp2 -= dano1 * 0.7
            elif ato1 == 4:
                hp1 += 150
                if status1 == '\033[1;32mEnvenenado\033[m':
                    status1 = '\033[1;37mNormal\033[m'
        if hp2 <= 0:
            break
    else:
        print(f'\033[1;33m{nomes[0]} está CONGELADO\033[m')
        cont1_gelo += 1
        sleep(1)
        print(f'Faltam {4 - cont1_gelo} rodadas para acabar...')
        if cont1_gelo == 3:
            status1 = '\033[1;37mNormal\033[m'
        sleep(1)
    if 500 >= hp1 > 250:
        print(f'{nomes[0]}: \033[1;32m{hp1}\033[m pontos de vida Status:{status1}')
    elif 250 >= hp1 > 135:
        print(f'{nomes[0]}: \033[1;33m{hp1}\033[m pontos de vida Status:{status1}')
    elif 135 >= hp1 > 0:
        print(f'{nomes[0]}: \033[1;31m{hp1}\033[m pontos de vida Status:{status1}')
    if 500 >= hp2 > 250:
        print(f'{nomes[1]}: \033[1;32m{hp2}\033[m pontos de vida Status:{status2}')
    elif 250 >= hp2 > 135:
        print(f'{nomes[1]}: \033[1;33m{hp2}\033[m pontos de vida Status:{status2}')
    elif 135 >= hp2 > 0:
        print(f'{nomes[1]}: \033[1;31m{hp2}\033[m pontos de vida Status:{status2}')
    print('=' * 37)
    if status2 != '\033[1;33mCongelado\033[m':
        print(f'Ataques disponiveis para o {nomes[1]}:')
        print(ações[1])
        ato2 = int(input('Qual será sua ação? ')) - 1
        sorte2 = randint(0, 9)
        if classes_jogadores[1] == 'Arqueiro':
            if ato2 != 4:
                crit2 = crit[sorte2]
                if crit2 == 1:
                    dano2 = dano_arqueiro[ato2] * 2
                    print('\033[1;31mCRITICO\033[m')
                else:
                    dano2 = dano_arqueiro[ato2]
            sleep(1)
            if ato2 != 4 and ato2 != 1:
                print(f'Habilidade usada: {Arqueiro[ato2]}')
                sleep(1)
                print(f'Dano causado: {dano2}')
            elif ato2 == 1:
                print(f'Habilidade usada: {Arqueiro[ato2]}')
                sleep(1)
                print(f'Dano causado: {dano2}')
                chance_ven2 = randint(0, 9)
                if ven[chance_ven2] == 1:
                    sleep(1)
                    print('\033[1;32mO inimigo ficou ENVENENADO\033[m')
                    sleep(1)
                    print('Causará um dano igual a 10% do Hp')
                    status1 = '\033[1;32mEnvenenado\033[m'
            elif ato2 == 4:
                print(f'Habilidade usada: {Arqueiro[ato2]}')
                sleep(1)
                print('Vida Recupurada: +150')
        elif classes_jogadores[1] == 'Paladino':
            dano2 = dano_paladino[ato2]
            sleep(1)
            if ato2 != 4 and ato2 != 1 and ato2 != 2:
                print(f'Habilidade usada: {Paladino[ato2]}')
                sleep(1)
                print(f'Dano causado: {dano2}')
            elif ato2 == 1:
                print(f'Habilidade usada: {Paladino[ato2]}')
                sleep(1)
                print(f'Dano Reduzido em 50%')
                status2 = '\033[1;35mProtegido\033[m'
            elif ato2 == 2:
                print(f'Habilidade usada: {Paladino[ato2]}')
                sleep(1)
                print(f'Ataque aumenta em 50%')
                status2 = '\033[1;31mPuto\033[m'
            elif ato2 == 4:
                print(f'Habilidade usada: {Paladino[ato2]}')
                sleep(1)
                print('Vida Recupurada: +150')
        elif classes_jogadores[1] == 'Mago':
            dano2 = dano_mago[ato2]
            sleep(1)
            if ato2 != 4 and ato2 != 0 and ato2 != 3 and ato2 != 2 and ato2 != 1:
                print(f'Habilidade usada: {Mago[ato2]}')
                sleep(1)
                print(f'Dano causado: {dano2}')
            elif ato2 == 0:
                print(f'Habilidade usada: {Mago[ato2]}')
                sleep(1)
                print(f'Dano causado: {dano2}')
                chance_fogo2 = randint(0, 9)
                if fogo[chance_fogo2] == 1:
                    if status1 != '\033[1;34mMolhado\033[m' and status1 != '\033[1;33mCongelado\033[m':
                        sleep(1)
                        print('\033[1;31mO inimigo está QUEIMANDO\033[m')
                        sleep(1)
                        print('Causará um dano redução de 30% do dano')
                        status1 = '\033[1;31mQueimando\033[m'
                    elif status1 == '\033[1;33mCongelado\033[m':
                        sleep(1)
                        print('O inimigo foi descongelado...')
                        status1 = '\033[1;37mNormal\033[m'
                    elif status1 == '\033[1;34mMolhado\033[m':
                        sleep(1)
                        print('O inimigo acabou de tomar uma sauna...')
                        sleep(1)
                        status1 = '\033[1;37mNormal\033[m'
            elif ato2 == 3:
                print(f'Habilidade usada: {Mago[ato2]}')
                sleep(1)
                print(f'Dano causado: {dano2}')
                sleep(1)
                if status1 != '\033[1;31mQueimando\033[m':
                    print('O inimigo está MOLHADO')
                    status1 = '\033[1;34mMolhado\033[m'
                else:
                    print('O inimigo acabou de tomar banho...')
                    status1 = '\033[1;37mNormal\033[m'
            elif ato2 == 1:
                print(f'Habilidade usada: {Mago[ato2]}')
                sleep(1)
                print(f'Dano causado: {dano2}')
                chance_gelo2 = randint(0, 9)
                if gelo[chance_gelo2] == 1:
                    if status1 == '\033[1;31mQueimando\033[m':
                        sleep(1)
                        print('O inimigo sentiu uma leve brisa resfriante')
                        status1 = '\033[1;37mNormal\033[m'
                    else:
                        sleep(1)
                        print('Inimigo CONGELADO')
                        status1 = '\033[1;33mCongelado\033[m'
                        sleep(1)
                        if status1 != '\033[1;34mMolhado\033[m':
                            cont1_gelo = 1
                        else:
                            cont1_gelo = 0
            elif ato2 == 2:
                if status1 != '\033[1;34mMolhado\033[m':
                    print(f'Habilidade usada: {Mago[ato2]}')
                    sleep(1)
                    print(f'Dano causado: {dano2}')
                else:
                    sleep(1)
                    print('\033[1;36mFoi realizado um ataque ELEMENTAL\033[m')
                    dano2 = dano2 * 2
                    sleep(1)
                    print(f'Habilidade usada: {Mago[ato2]}')
                    sleep(1)
                    print(f'Dano causado: {dano2}')
                    status1 = '\033[1;37mNormal\033[m'
            elif ato2 == 4:
                print(f'Habilidade usada: {Mago[ato2]}')
                sleep(1)
                print('Vida Recupurada: +150')
        elif classes_jogadores[1] == 'Assassino':
            dano2 = dano_assassino[ato2]
            sleep(1)
            if ato2 != 4 and ato2 != 1 and ato2 != 3:
                print(f'Habilidade usada: {Assassino[ato2]}')
                sleep(1)
                print(f'Dano causado: {dano2}')
            elif ato2 == 1:
                print(f'Habilidade usada: {Assassino[ato2]}')
                sleep(1)
                print(f'Dano causado: {dano1}')
                chance_ven1 = randint(0, 9)
                if ven[chance_ven1] == 1:
                    sleep(1)
                    print('\033[1;32mO inimigo ficou ENVENENADO\033[m')
                    sleep(1)
                    print('Causará um dano igual a 1% do Hp')
                    status1 = '\033[1;32mEnvenenado\033[m'
            elif ato2 == 3:
                sleep(1)
                print('Primeira adaga lançada...')
                adaga1 = randint(20, 40)
                sleep(1)
                print(f'Dano: {adaga1}')
                sleep(1)
                print('Segunda adaga lançada...')
                sleep(1)
                adaga2 = randint(20, 40)
                print(f'Dano: {adaga2}')
                sleep(1)
                dano2 = adaga1 + adaga2
                print(f'Dano total: {dano2}')
                sleep(1)
            elif ato2 == 4:
                print(f'Habilidade usada: {Assassino[ato2]}')
                sleep(1)
                print('Vida Recupurada: +150')
        rod += 1
        if status1 == '\033[1;35mProtegido\033[m':
            hp1 -= ceil((dano2/2))
            cont1 += 1
            if cont1 == 3:
                print('\033[1;35mBUFF de defesa acabou\033[m')
                print('=' * 37)
                status1 = '\033[1;37mNormal\033[m'
        else:
            if ato2 != 4:
                if status2 == '\033[1;37mNormal\033[m' or status2 == '\033[1;34mMolhado\033[m':
                    hp1 -= dano2
                if status1 == '\033[1;32mEnvenenado\033[m':
                    hp1 -= ceil(0.01*hp1)
                elif status2 == '\033[1;31mQueimando\033[m':
                    hp1 -= dano2 * 0.7
            elif ato2 == 4:
                hp2 += 150
                if status2 == '\033[1;32mEnvenenado\033[m' or '\033[1;31mQueimando\033[m':
                    status2 = '\033[1;37mNormal\033[m'
        if hp1 <= 0:
            break
    else:
        print(f'\033[1;33m{nomes[1]} está CONGELADO\033[m')
        cont2_gelo += 1
        sleep(1)
        print(f'Faltam {4 - cont2_gelo} rodadas para acabar...')
        if cont2_gelo == 3:
            status2 = '\033[1;37mNormal\033[m'

print('Fim da batalha')
sleep(1)
if hp1 > 0:
    print(f'O vencedor foi {nomes[0]}')
else:
    print(f'O vencedor foi {nomes[1]}')
