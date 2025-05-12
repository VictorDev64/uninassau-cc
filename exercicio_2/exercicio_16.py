#Faça um algoritmo que leia três valores que representam os três lados de um triângulo e verifique se são válidos,
#determine se o triângulo é equilátero, isósceles ou escaleno.

lado1 = int(input('Digite o primeiro lado do triângulo: '))
lado2 = int(input('Digite o segundo lado do triângulo: '))
lado3 = int(input('Digite o terceiro lado do triângulo: '))

if lado1 + lado2 > lado3 and lado2 + lado3 > lado1 and lado3 + lado1 > lado2:
   print('Seu triângulo é válido!')
   if lado1 == lado2 == lado3:
      print('Seu triângulo é equilátero.')
   elif lado1 == lado2 or lado2 == lado3 or lado1 == lado3:
      print('Seu triângulo é isósceles.')
   else:
      print('Seu triângulo é escaleno.')
else:
   print('Seu triângulo não existe, tente novamente.')