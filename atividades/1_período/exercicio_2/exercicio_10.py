#Faça um algoritmo que leia três notas obtidas por um aluno, e imprima na tela a média das notas.

nota_1 = float(input('Insira a primeira nota do aluno: '))
nota_2 = float(input('Insira a segunda nota do aluno: '))
nota_3 = float(input('Insira a terceira nota do aluno: '))

media = (nota_1+nota_2+nota_3) / 3
print(f'A média de suas notas é: {media:.1f}')