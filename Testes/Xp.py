xp = 300
level = 0
for c in range(1, 101):
    if xp >= c*100:
        print('\033[1;33mLevel up\033[m')
        level = c
        xp = xp - c*100
print('Nível: {}'.format(level))
print('Seu Xp atual é: {}'.format(xp))
