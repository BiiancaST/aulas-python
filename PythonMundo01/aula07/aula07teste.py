nome= input('Qual o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome))
print('Prazer em te conhecer {:>20}!'.format(nome))
print('Prazer em te conhecer {:<20}!'.format(nome))
print('Prazer em te conhecer {:^20}!'.format(nome))
print('Prazer em te conhecer {:=^20}!'.format(nome))

n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s= n1+n2
m= n1*n2
d= n1/n2
di= n1//n2
p= n1**n2
print('A soma é {}, o produto é {} e a divisão é {:.2f}!'.format(s, m, d))
print('A divisão inteira {} e potência {}!'.format(di, p))
print('A soma é {}, o produto é {} e a divisão é {:.2f}!'.format(s, m, d), end=' ')
print('A divisão inteira {} e potência {}!'.format(di, p))
print('A soma é {},\n o produto é {}\n e a divisão é {:.2f}!'.format(s, m, d))
print('A divisão inteira {} \ne potência {}!'.format(di, p))
