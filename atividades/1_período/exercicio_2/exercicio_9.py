#Faça um algoritmo que calcule o imc (Índice de Massa Corporal) de uma pessoa, leia o seu peso e sua altura e imprima na tela sua
#condição de acordo com a tabela abaixo: 

#Fórmula do imc = peso / (altura)²

#Tabela Condições imc
#Abaixo de 18,5 | Abaixo do peso
#Entre 18,6 e 24,9 | Peso ideal (parabéns)
#Entre 25,0 e 29,9 | Levemente acima do peso
#Entre 30,0 e 34,9 | Obesidade grau I
#Entre 35,0 e 39,9 | Obesidade grau II (severa)
#Maior ou igual a 40 | Obesidade grau III (mórbida)

peso = float(input('Insira seu peso em kg: '))
altura = float(input('Insira sua altura em m: '))
imc = peso/(altura**2)
print(f'Seu IMC é de: {imc:.1f}')

if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc < 24.9:
    print('Você está no peso ideal!')
elif imc < 29.9:
    print('Você está levemente acima do peso.')
elif imc < 34.9:
    print('Você está em obesidade grau I.')
elif imc < 39.9:
    print('Você está em obesidade grau II.')
else:
    print('Você está em obesidade grau III.')