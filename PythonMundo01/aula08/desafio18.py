#faça um programa que leia um angulo qualquer e mostre
#na tela o valor do seno, cosseno e tangente desse angulo
import math
ang= float(input('qual o angulo? '))
seno= math.sin(math.radians(ang))
print(f'o angulo de {ang} tem o seno de {seno:.2f}')
cosseno= math.cos(math.radians(ang))
print(f'o angulo de {ang} tem o cosseno de {cosseno:.2f}')
tang= math.tan(math.radians(ang))
print(f'o angulo de {ang} tem a tangente de {tang:.2f}')
