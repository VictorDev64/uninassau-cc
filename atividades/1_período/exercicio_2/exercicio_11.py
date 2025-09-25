#Faça um algoritmo que leia quatro notas obtidas por um aluno, calcule a média das nota obtidas, imprima na tela o nome do aluno 
#e se o aluno foi aprovado ou reprovado. Para o aluno ser considerado aprovado sua média final deve ser maior ou igual a 7.

nome = input('Insira o nome do aluno: ')
nota_1 = float(input('Insira a primeira nota do aluno: '))
nota_2 = float(input('Insira a segunda nota do aluno: '))
nota_3 = float(input('Insira a terceira nota do aluno: '))
nota_4 = float(input('Insira a quarta nota do aluno: '))

media = (nota_1+nota_2+nota_3+nota_4) / 4

if media >= 7:
    print(f'O aluno {nome} foi aprovado com média {media:.1f}.')
else:
    print(f'O aluno {nome} foi reprovado com média {media:.1f}.')