#Faça um algoritmo que leia dois valores inteiros A e B, se os valores de A e B forem iguais, deverá somar os dois valores,
#caso contrário deverá multiplicar A por B. Ao final de qualquer um dos cálculos deve-se atribuir o resultado a uma
#variável C e imprimir seu valor na tela.
    
a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))

if a==b:
   c = a+b
   print(f'A e B são iguais. Sua variável C é: {c}')
else:
   c = a*b
   print(f'A e B são diferentes. Sua variável C é: {c}')