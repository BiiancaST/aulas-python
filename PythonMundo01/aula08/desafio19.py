import random

# um professor quer sortear um dos seus quatro alunos para apagar o quadro
# faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido

n = input('primeiro aluno: ')
n2 = input('segundo aluno: ')
n3 = input('terceiro aluno: ')
n4 =  input('quarto aluno: ')
lista =  [n, n2, n3, n4]
print('o escolhido foi: {}'.format(random.choice(lista)))

