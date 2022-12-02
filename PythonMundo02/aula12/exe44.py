print('{:=^60}'.format('LOJAS GUANABARA'))
dinheiro = float(input('Por favor vendedor digite aqui o total a pagar: R$ '))
op = str(input("""Qual será a forma de pagamento escolhida pelo cliente? 
Opção 1: A vista em dinheiro ou cheque
Opção 2: A vista no cartão
Opção 3: Em até 2x no cartão sem juros
Opção 4: Em mais vezes no cartão com 20% de juros
Digite o numero da opção escolhida: """))
if op == '1':
    desc = dinheiro * 10 / 100
    pagamento = dinheiro - desc
    print('O desconto foi de R$ {:.2f}, o total a ser pago é R$ {:.2f}'.format(desc, pagamento))
elif op == '2':
    desc = dinheiro * 5 / 100
    pagamento = dinheiro - desc
    print(f'O desconto foi de R$ {desc:.2f}, o total a ser pago é R$ {pagamento:.2f}')
elif op == '3':
    pagamento = dinheiro / 2
    print(f'O total de R$ {dinheiro:.2f} foi parcelado em 2x,as parcelas ficaram no valor de R$ {pagamento:.2f}')
elif op == 4:
    parcela = int(input('Em quantas vezes o cliente gostaria de parcelas? '))
    juros = dinheiro * 20 / 100
    j = dinheiro + juros
    p = j / parcela
    print(f'Serão {parcela} parcelas de R$ {p:.2f}, totalizando R$ {j:.2f}')
else:
    print('Opção invalida. TENTE NOVAMENTE!')