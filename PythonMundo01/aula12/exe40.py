print('\033[1mVamos calcular a média do aluno!\033[m')
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('\033[31;1mSua média foi {}, você está REPROVADO'.format(media))
elif media == 5 or media < 7:
    print('\033[33;1mSua média foi {}, você está de RECUPERAÇÃO, boa sorte!'.format(media))
else:
    print('\033[32mParabéns!!! Sua média foi {}, você está APROVADO!!! Boas férias!!!'.format(media))
