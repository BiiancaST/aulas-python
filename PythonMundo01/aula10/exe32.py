ano = int(input('Em que ano estamos? '))
bix = ano % 4
if bix == 0:
    print('Estamos em um ano bissexto')
else:
    print('Não estamos em um ano bissexto')
