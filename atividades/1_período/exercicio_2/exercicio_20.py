#Faça um algoritmo que receba um valor inteiro e imprima na tela a sua tabuada.

a = int(input('Insira seu número: '))

print('Aqui está sua tabuada:')
for i in range(1, 11):
    print(f'{a} x {i} = {a*i}')