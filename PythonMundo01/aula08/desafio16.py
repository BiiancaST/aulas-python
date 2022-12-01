#crie um programa que leia um numero real qualquer pelo teclado
#e mostre na tela sua porção inteira
#ex: digite um numero: 6.127
#o numero 6.127 tem a parte inteira 6.
import math
n= float(input('digite um numero: '))
print('a resposta correta para o exercico é esta {}'.format(math.trunc(n)))
print('o numero {} tem a parte inteira {}'.format(n, math.floor(n)))
print('se arredondar para cima o numero seria {}'.format(math.ceil(n)))
#print('a sua porção inteira é {}'.format(n, math.trunc(n)))
#o correto neste exercicio é o trunc, pois ele puxa apenas a porção inteira do numero
#os outros apenas arredondam, o resultado não dará certo com numero negativos

