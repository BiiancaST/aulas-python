from random import randint
print('-*-'*20)
print('BEM VINDO JOGADOR')
print('-*-'*20)
escolha = int(input('escolha seu dado: '))
dado = randint(0,escolha)
print(f'O dado escolhido foi D{escolha} e o numero sorteado foi {dado}')
