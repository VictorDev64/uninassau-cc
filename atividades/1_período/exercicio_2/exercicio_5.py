#Faça um algoritmo que leia o valor do salário mínimo e o valor do salário de um usuário, calcule quantos salários mínimos esse 
#usuário ganha e imprima na tela o resultado. (Base para o salário mínimo: R$ 1.518,00).

salário_min = 1518.00
salário_user = float(input('Insira seu salário: '))
quantia = salário_user / salário_min

print(f'Seu salário equivale a {quantia:.2f} salários mínimos.')