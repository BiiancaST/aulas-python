print('\033[1;32;44mOlá mundo!\033[m')
a = 3
b = 5
print(f'Os valores são \033[32m{a}\033[m e \033[31m{b} \033[m')

cores = {'limpa' :'\033[m',
         'vermelho':'\033[31m',
         'amarelo':'\033[33m',
         'invertido':'\033[7;37m'}
print('Os valores {}{}{} e {}{}{}'.format(cores['vermelho'], b, cores['limpa'], cores['invertido'], a, cores['limpa']))
