viagem = float(input('Quantos km tem a viagem? '))
if viagem <= 200:
    pa = (1/2)*viagem
    print('Sua passagem custará R${:.2f}'.format(pa))
else:
    pas = viagem*0.45
    #print(pas)
    print('Sua passagem custará R${:.2f}'.format(pas))
#PREÇO = DISTANCIA * 0.50 IF DISTANCIA <= 200 ELSE DISTANCIA * 0.45 (modo simpificado)
'''outro modo de fazer
if distancia <= 200:
preço = distancia * 0.50
else:
preço = disntancia * 0.45
print(fSua passagem custará R$ {preço:.2f}'''