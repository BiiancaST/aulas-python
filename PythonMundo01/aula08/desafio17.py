#faça um programa que leia o comprimento do cateto
#oposto e do cate adjacente de um triangulo retangulo,
#calcule e mostre o comprimento da hipotenusa
import math
oposto= float(input('cateto oposto: '))
adj= float(input('cateto adjacente: '))
print('o comprimento da hipotesuna: {:.2f}'.format(math.hypot(oposto, adj)))

#a maneira matematica de fazer o exercicio é:
#hipotenusa = (oposto**2 + adj**2) ** (1/2)
