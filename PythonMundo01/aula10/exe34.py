sal = float(input('Quanto você ganha? R$ '))
if sal <= 1250:
    a = (sal*15)/100
    print(f'Seu aumento será de R$ {a:.2f} e seu salario ficará no valo de R$ {sal+a:.2f}')
else:
    au = (sal*10)/100
    print(f'Seu aumento será de R$ {au:.2f} e seu salario ficará no valor de R$ {sal+au:.2f}')

'''if salario <= 1250:
novo = salario + ( salario * 15 / 100)
else:
novo = salario + ( salario * 10 / 100)
print(f Quem ganhava R$ {sal:.2f} passa a ganhar R$ {novo:.2f})'''
