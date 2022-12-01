print('Crie um algoritmo que leia um numero e mostre o seu dobro, triplo e raiz quadrada')
n = int(input('Digite um numero de dois digitos: '))
d = n*2
t = n*3
r = n**(1/2)
print('O dobro é {}.\nTriplo é {}\nE a raiz quadrada é {:.2f}!'.format(d, t, r))
print('O dobro é {}, o triplo é {} e a raiz {}!'.format((n*2), (n*3), pow(n, (1/2))))
