from random import randint
level = 0
for c in range(1, 5):
    xp = randint(30, 50)
    level += xp
    if level >= 100:
        print('Level up')
        print('Nível: 2')
        level = 0
print('Sua exp agr é {}'.format(level))
for c in range(1, 5):
    xp = randint(30,50)
    level += xp
    if level >= 200:
        print('Level up')
        print('Nível: 3')
        level = 0
print('Sua exp agr é {}'.format(level))
