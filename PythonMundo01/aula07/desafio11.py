print('Faça um programa que leia a largura e a altura de uma parede em metros, calcule sua area e a quantidade de tinta\n necessariapara pinta-la sabendo que cada litro de tinta cobre 2m²')
larg = float(input('Largura: '))
alt = float(input('Altura: '))
print('Seu metro quadrado: {}'.format(larg*alt))
print('Serão necessaria {} litros de tinta'.format((alt*larg)/2))
