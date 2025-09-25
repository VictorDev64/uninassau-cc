#Faça algoritmo que leia o nome e a idade de uma peso e imprima na tela o nome da pessoa e se ela é maior ou menor de idade.

nome = input('Insira seu nome: ')   
idade = int(input('Insira sua idade: '))

if idade >= 18:
    print(f'{nome}, você é maior de idade.')
else:
    print(f'{nome}, você é menor de idade.')