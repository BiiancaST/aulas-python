from random import randint
from time import sleep

cores = {'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'lilas': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m',
         'limpa': '\033[m'}

computador = randint(0, 5)
print('\033[34m-=-\033[m' * 20)
print('{}Vou pensar em um número entre 0 e 5. Tente adivinhar...{}'.format(cores['lilas'], cores['limpa']))
print('\033[36m-=-\033[m' * 20)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(3)
if jogador == computador:
    print('{}Parabéns! Você conseguiu me vencer!{}'.format(cores['verde'], cores['limpa']))
else:
    print(f'\033[31mGanhei! Eu pensei no número {computador} e não no {jogador}!\033[m')
