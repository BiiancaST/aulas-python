from datetime import date
atual = date.today().year
ano = int(input('Em qual ano nasceu o atleta? '))
idade = atual - ano
print(f'O atleta tem {idade} anos')
if idade <= 9:
    print('\033[36mClassificação: Atleta Mirim')
elif idade <= 14:
    print('\033[35mClassificação: Atleta Infantil')
elif idade <= 19:
    print('\033[34;4mClassificação: Atleta Junior')
elif idade == 20:
    print('\033[37;3mClassificação: Atleta Sênior\033[m')
else:
    print('\033[37;9mClassificação: Atleta Master\033[m')