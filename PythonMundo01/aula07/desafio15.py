dias = int(input('por quantos dias o carro foi alugado? '))
km = float(input('quantos km fora rodados? '))
total = (dias * 60) + (km * 0.15)
print('o total a pagar será R$ {:.2f}'.format(total))
