#Classes: Mago, Arqueiro, Paladino, Héroi, Assasino
itens_mago = ['Cajado', 'Varinho', 'Livro']
itens_arqueiro = ['Arco Curto', 'Besta', 'Arco Longo']
itens_paladino = ['Espada Longa', 'Escudo', 'Machado']
itens_heroi = ['Espada', 'Escudo']
itens_assasino = ['Adaga de uma mão', 'Adaga de duas mãos']
print('Os itens de mago são: {}'.format(itens_mago))
print('Os itens de arqueiro são: {}'.format(itens_arqueiro))
print('Os itens de paladino são: {}'.format(itens_paladino))
print('Os itens de heroi são: {}'.format(itens_heroi))
print('Os itens de assasino são: {}'.format(itens_assasino))
escolha = str(input('Qual o seu item? ')).strip().lower().title()
if escolha == 'Cajado':
    dano = 30
    crit = 0.1
elif escolha == 'Varinha':
    dano = 10
    crit = 0.5
elif escolha == 'Livro':
    dano = 20
    crit = 0.2
elif escolha == 'Arco Curto':
    dano = 20
    crit = 0.2
elif escolha == 'Besta':
    dano = 30
    crit = 0.1
elif escolha == 'Arco Longo':
    dano = 40
    crit = 0
elif escolha == 'Espada Longa':
    dano = 25
    crit = 0.4
elif escolha == 'Machado':
    dano = 40
    crit = 0.1
elif escolha == 'Espada':
    dano = 15
    crit = 0.7
elif escolha == 'Adaga':
    pergunta = input('Uma ou duas mãos? ').strip().lower().title()
    if pergunta == 'Uma':
        dano = 40
        crit = 0.25
    elif pergunta == 'Duas':
        dano = 20
        crit = 0.5
print('O dano é {}'.format(dano))
print('A chance de critico é {}'.format(crit))
#Fazer os itens com classificação: Comun,Raro,Lendário,Mitico
#Depedendo da classicação multiplica o dano base da arma comum * 1, raro * 2, lend * 3 mit * 4
#Status???
raridade = 'Comum'
if raridade == 'Lendário':
    print('\033[33m')
if raridade == 'Comum':
    print('\033[32m')
print(raridade)
