salario= float(input('qual o salario do funcionario? R$ '))
novo= salario + (salario*15/100)
print('o salario de {:.2f} com o aumento de 15% ficou {:.2f}'.format(salario, novo))
