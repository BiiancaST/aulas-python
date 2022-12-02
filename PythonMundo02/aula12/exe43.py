print('Vamos calcular o seu IMC?')
peso = float(input('Digite seu peso em kilos: '))
altura = float(input('Digite seu altura em metros: '))
imc = peso / (altura * altura)
print(f'Seu IMC é de {imc:.2f}')
if imc < 18.5:
    print('\033[33mCUIDADO! Você está abaixo do peso')
elif 18.5 <= imc < 25:
    print('\033[32mPARABÉNS! Você está no peso ideal!')
elif 25 <= imc < 30:
    print('\033[34mATENÇÃO! Você está com sobrepeso')
elif 30 <= imc < 40:
    print('\033[31mCUIDADO!!! Você está com obesidade, procure um médico!')
else:
    print('\033[1;31mCUIDADO!!! VocÊ está com OBESIDADE MÓRBIDA, procure URGENTE um médico!!!')
