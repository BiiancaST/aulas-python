casa = float(input('Valor da casa: R$ '))
salario = float(input('Salario do comprador: R$ '))
anos = int(input('Em quantos anos pretende quitar o valor? '))
meses = anos * 12
parcela = casa / meses
n = salario*30/100
if parcela <= n:
    print(f"""Parabéns o seu emprestimo foi aprovado:
    Serão {meses} parcelas, no valor de R${parcela:.2f}""")
else:
    print(f"""Seu emprestimo foi negado:
    Infelizmente a parcela de R$ {parcela:.2f} excedeu o limite de 30% de seu salario, a parcela minima seria de R$ {n:.2f}""")
#print(n)
