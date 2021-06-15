from random import randint
from time import sleep
#Combate com algum inimigo
ação = '''[ 1 ] - Soco
[ 2 ] - Atirar Pedra
Qual será sua ação? '''
ataque = 0
dano_heroi = 10
nome = str(input('Digite o nome do seu personagem: ')).strip().lower().title()
inimigos = ('Slime', 'Esqueleto', 'Zumbi')
itens = ('Espada', 'Machado', 'Espada Longa', 'Cajado', 'Varinha', 'Livro', 'Arco Curto', 'Arco longo', 'Besta', 'Adaga')
chance_drop = randint(0, 8)
drop = itens[chance_drop]
if drop == 'Cajado':
    dano_iten = 30
elif drop == 'Varinha':
    dano_iten = 10
elif drop == 'Livro':
    dano_iten = 20
elif drop == 'Arco Curto':
    dano_iten = 20
elif drop == 'Besta':
    dano_iten = 30
elif drop == 'Arco Longo':
    dano_iten = 40
elif drop == 'Espada Longa':
    dano_iten = 25
elif drop == 'Machado':
    dano_iten = 40
elif drop == 'Espada':
    dano_iten = 15
elif drop == 'Adaga':
    pergunta = input('Uma ou duas mãos? ').strip().lower().title()
    if pergunta == 'Uma':
        dano_iten = 40
    elif pergunta == 'Duas':
        dano_iten = 20
random = randint(0, 2)
aparecer = inimigos[random]
vida_inimigo : int = 20
vida_heroi: int = 100
if aparecer == 'Slime':
    ataque_inimigo = ('Jogar gosma', 'Investida')
    chance = randint(0,1)
    turno = ataque_inimigo[chance]
    if chance == 0:
        atacou ='Jogou uma gosma'
    elif chance == 1:
        atacou = 'Deu uma investida'
elif aparecer == 'Esqueleto':
    ataque_inimigo = ('Ossada', 'Atira flecha')
    chance = randint(0,1)
    turno = ataque_inimigo[chance]
    if chance == 0:
        atacou = 'Deu uma ossada'
    elif chance == 1:
        atacou = 'Atirou uma flecha'
elif aparecer == 'Zumbi':
    ataque_inimigo = ('Mordida', 'Grunido')
    chance = randint(0,1)
    turno = ataque_inimigo[chance]
    if chance == 0:
        atacou = 'Deu uma mordida'
    elif chance == 1:
        atacou = 'Deu um grunido'
for b in range(0, 3):
    combate = str(input('''Um {} apareceu, deseja enfrenta-ló?
Sim ou Não? '''.format(aparecer))).strip().lower().replace('a', 'ã')
    if combate == 'não':
        print('Você fugiu do inimigo')
    elif combate == 'sim':
        if vida_inimigo > 0:
            aparecer = inimigos[random]
            print('{}: \033[33m{}\033[m pontos de vida'.format(aparecer, vida_inimigo))
            print('=' * 28)
            if 100 >= vida_heroi > 60:
                hp = ('\033[1;32m{}\033[m'.format(vida_heroi))
            elif 60 >= vida_heroi >= 30:
                hp = ('\033[1;33m{}\033[m'.format(vida_heroi))
            elif 29 >= vida_heroi >= 1:
                hp = ('\033[1;31m{}\033[m'.format(vida_heroi))
            elif vida_heroi < 1:
                hp = ('\033[1;37m{}\033[m'.format(vida_heroi))
            print('{}: {} pontos de vida'.format(nome, hp))
            print('-' * 28)
            print('\033[1;32mSeu Turno\033[m')
            ato = int(input(ação))
            sleep(1)
        if ato == 1:
                print('{} meteu um soco no {}'.format(nome, aparecer))
                lista = ('1', '1', '1', '0', '0', '1', '0', '1', '1', '1')
                ran = randint(0, 9)
                crit = lista[ran]
                if crit == '1':
                    dano_heroi = 10
                elif crit == '0':
                    print('\033[1;31mCRITICO\033[m')
                    dano_heroi = 2 * dano_heroi
        elif ato == 2:
            print('{} jogou uma pedra no {}'.format(nome, aparecer))
            lista = ('1', '1', '1', '0', '0', '1', '0', '1', '1', '1')
            ran = randint(0, 9)
            crit = lista[ran]
            if crit == '1':
                dano_heroi = 5
            elif crit == '0':
                print('\033[1;31mCRITICO\033[m')
                dano_heroi = dano_heroi
        elif ato == 3:
            print('{} Ultilizou sua arma no {}'.format(nome, aparecer))
            lista = ('1', '1', '1', '0', '0', '1', '0', '1', '1', '1')
            ran = randint(0, 9)
            crit = lista[ran]
            if crit == '1':
                dano_heroi = dano_iten
            elif crit == '0':
                print('\033[1;31mCRITICO\033[m')
                dano_heroi = 2 * dano_iten
        sleep(2)
        print('Isso causou \033[34m{}\033[m de dano'.format(dano_heroi))
        sleep(2)
        nova_vida_inimigo = vida_inimigo - dano_heroi
        print('-' * 28)
        print('{}: \033[33m{}\033[m pontos de vida'.format(aparecer, nova_vida_inimigo))
        print('=' * 28)
        print('{}: {} pontos de vida'.format(nome, hp))
        print('-' * 28)
        sleep(2)
        if nova_vida_inimigo > 0:
            print('\033[1;33mTurno do Inimigo\033[m')
            sleep(2)
            print('{} {} em {}'.format(aparecer, atacou, nome))
            sleep(2)
            ataque = randint(1, 20)
            print('Isso causou \033[1;31m{}\033[m de dano'.format(ataque))
            print('-' * 28)
            sleep(2)
            nova_vida_heroi = vida_heroi - ataque
        else:
            print('Inimigo está morto')
            sleep(1)
            print('Fim da batalha')
            sleep(1)
            print('O inimigo dropou um \033[1;32m{}\033[m'.format(drop))
            sleep(1)
            print('O dano do iten é {}'.format(dano_iten))
            equip = input('Deseja equipa-ló? ').strip().lower()
            if equip == 'sim':
                print('Você agora pode atacar com sua arma')
                ação = '''[ 1 ] - Soco
[ 2 ] - Atirar Pedra
[ 3 ] - Usar arma
Qual será sua ação? '''
            else:
                print('Iten não equipado')
        if ataque > 0:
            vida_heroi = nova_vida_heroi
        else:
            vida_heroi = vida_heroi
        vida_inimigo = nova_vida_inimigo
else:
    vida_inimigo = 30
    random = randint(0, 2)
    aparecer = inimigos[random]
    chance_drop = randint(0, 8)
    drop = itens[chance_drop]
