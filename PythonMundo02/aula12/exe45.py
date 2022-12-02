import random
from time import sleep
print('\033[7;30M-+-'*20)
print('{:=^60}'.format(' BEM VINDO JOGADOR '))
print('-+-\033[m'*20)
j = str(input('\033[1;35mPedra, Papel ou Tesoura? \033[m')).strip().lower()
j2 = ['pedra', 'papel', 'tesoura']
computador = random.choice(j2)
#print(computador)
print('\033[35;1mPROCESSANDO...\033[m')
sleep(2)
print(f'Eu escolhi {computador}')
if computador == 'pedra' and j == 'tesoura':
    print('\033[31;1mEu ganhei!')
elif computador == 'pedra' and j == 'papel':
    print('\033[32;1mVocê ganhou!')
elif computador == 'papel' and j == 'pedra':
    print('\033[31;1mEu ganhei!')
elif computador == 'papel' and j == 'tesoura':
    print('\033[32;1mVocê ganhou!')
elif computador == 'tesoura' and j == 'papel':
    print('\033[31;1mEu ganhei!')
elif computador == 'tesoura' and j == 'pedra':
    print('\033[32;1mVocê ganhou!')
else:
    print('\033[33;1mEMPATE\033[m')
print('\033[35mDeseja jogar novamente?')
