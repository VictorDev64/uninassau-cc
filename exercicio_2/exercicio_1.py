#Faça um algoritmo que leia os valores de A, B, C e em seguida imprima na tela a soma entre A e B é mostre se a soma é menor que C.
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))
print(f'Soma de A + B: {a+b}')

if a+b==c:
   print('Tal soma é igual a C.')
elif a+b<c:
   print('Tal soma é menor que C.')
else:
   print('Tal soma é maior que C.')