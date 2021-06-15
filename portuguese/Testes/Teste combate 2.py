from random import randint
Hp : int = 100
if 100>= Hp > 60:
    print('\033[1;32m{}\033[m'.format(Hp))
elif 60 >= Hp >= 30:
    print('\033[1;33m{}\033[m'.format(Hp))
elif 29 >= Hp >= 1:
    print('\033[1;31m\033[m'.format(Hp))
elif Hp == 0:
    print('\033[1;37mVocê está morto\033[m')
print(Hp)
calculo_vida : int
lista = ('1','1','1','0','0','1','0','1','1','1')
ran = randint(0,9)
crit = lista[ran]
if crit == '1':
    dano = 10
elif crit == '0':
    print('\033[1;31mCRITICO\033[m')
    dano = 20
print(dano)





