#escreva um programa que faça o computador pensar em um numero inteiro
#entre 0 e 5 e peça para o usuario tentar descobri

import random
print('Escolha um numero de 0 a 5 e tente adivinhar meu pensamento')
n = [0,1,2,3,4,5]
nu = random.choice(n)
#print(nu)
sorte = int(input('Digite um numero: '))
if sorte == nu:
    print('Parabens você acertou!')
else:
    print('Você perdeu!')
