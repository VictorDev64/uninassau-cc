#Faça um algoritmo que receba um valor A e B, e troque o valor de A por B e o valor de B por A e imprima na tela os valores.

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))

print('Trocando valores...')
a, b = b, a

print(f'Valor de A: {a}')
print(f'Valor de B: {b}')