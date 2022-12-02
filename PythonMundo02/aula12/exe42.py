r1 = float(input('Qual o tamanho do primeiro lado? '))
r2 = float(input('Qual o tamanho do segundo lado? '))
r3 = float(input('Qual o tamanho do terceiro lado? '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Essas medidas foraram um triangulo ', end ='')
    if r1 == r2 and r2 == r3 and r3 == r1:
    #GUANABARA: if r1 == r2 == r3:
        print('Equilatero!')
    elif r1 == r2 or r2 == r3 or r3 == r1:
    #esse ficou por ultimo com o else
        print('Isoseles!')
    else:
    #GUANABARA: elif r1 != r2 != r3 != r1:
        print('Escaleno!')
else:
    print('Com essas medidas não será possivel formar um triangulo')