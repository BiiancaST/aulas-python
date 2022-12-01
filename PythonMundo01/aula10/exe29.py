km = int(input('Qual a velocidade do carro? '))
if km > 80:
    multa = (km - 80) * 7
    print('Você foi excedeu o limite de 80km/h e foi MULTADO! \nSua multa é de R$ {},00'.format(multa))
else:
    print('Você esta dentro da velocidade permitida')
print('Dirija com segurança! Tenha um bom dia')
