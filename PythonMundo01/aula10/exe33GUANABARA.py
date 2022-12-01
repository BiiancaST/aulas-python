cores = {'branco': '\033[30m',
         'vermelho': '\033[31m',
         'verde': '\033[32m',
         'amarelo': '\033[33m',
         'azul': '\033[34m',
         'lilas': '\033[35m',
         'ciano': '\033[36m',
         'cinza': '\033[37m',
         'limpa': '\033[m'}
a = int(input('{}Primeiro valor: '.format(cores['ciano'])))
b = int(input('{}Segundo valor: '.format(cores['lilas'])))
c = int(input('{}Terceiro valor: {}'.format(cores['amarelo'], cores['limpa'])))
# verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
# verificando quem é o maior
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O menor valor digitado foi {menor}.')
print(f'O maior valor digitado foi {maior}.')
