import datetime
pessoa = int(input('Em que ano vc nasceu? '))
ano = date.today()year
ex = pessoa - ano
if ex < 18:
    print('Ainda não esta no tempo de você se alistar no exercito, faltam {} anos.'.format(ex))
elif ex = 18:
    print('Esta na hora de você se alistar no exercito!')
else:
    print('Já fazem {} anos que você se alistou no exercito.'format(ex))
