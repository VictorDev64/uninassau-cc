#Faça um algoritmo para receber um número qualquer e imprimir na tela se o número é par ou ímpar, positivo ou negativo.

a = int(input('Digite um número: '))

if a==0 or a%2==0:
   print('Seu número é par.')
else:
   print('Seu número é ímpar.')

if a>=0:
   print('Seu número é positivo.')
else:
   print('Seu número é negativo.')