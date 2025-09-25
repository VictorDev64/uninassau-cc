#Faça um algoritmo que leia uma temperatura em Fahrenheit e calcule a temperatura correspondente em grau Celsius. 
#Imprima na tela as duas temperaturas. 
#Fórmula: C = (5 * (F-32) / 9)

fahrenheit = float(input('Insira sua temperatura em Fahrenheit: '))
celsius = (5 * (fahrenheit - 32) / 9)

print(f'Sua temperatura em {fahrenheit}ºF equivale a {celsius:.1f}°C.')