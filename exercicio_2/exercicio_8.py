#Faça um algoritmo que leia três valores inteiros diferentes e imprima na tela os valores em ordem decrescente.

a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))

if a < c:
    a, c = c, a

if a < b:
    a, b = b, a

if b < c:
    b, c = c, b

print(f'A ordem decrescente é {a}, {b} e {c}.')