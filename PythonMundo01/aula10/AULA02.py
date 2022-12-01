nome = str(input('Qual o seu nome? ')).strip().lower()
if nome == 'anakin':
    print('Que nome lindo você tem <3')
else:
    print('Seu nome é tão normal :c')
print(f'Boa noite, {nome}!')

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n = (n1+n2)/2
print(f'A sua média foi {n:.2f}')
if n >= 6:
    print('Sua média foi boa! PARABÉNS!')
else:
    print('Sua média foi ruim! ESTUDE MAIS!')

#print('PARABENS' if n >= 6.0 else 'ESTUDE MAIS')