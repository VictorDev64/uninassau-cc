#Faça um algoritmo que leia o valor de um produto e determine o valor que deve ser pago, conforme a escolha da forma de pagamento
#pelo comprador e imprima na tela o valor final do produto a ser pago. Utilize os códigos da tabela de condições de pagamento para
#efetuar o cálculo adequado.

#Tabela de Código de Condições de Pagamento
#1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto
#2 - À Vista no cartão de crédito, recebe 10% de desconto
#3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros
#4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%

preço = float(input('Insira o valor do produto: '))
print('Escolha a forma de pagamento:')
print('1 - À Vista em Dinheiro ou Pix, recebe 15% de desconto')
print('2 - À Vista no cartão de crédito, recebe 10% de desconto')
print('3 - Parcelado no cartão em duas vezes, preço normal do produto sem juros')
print('4 - Parcelado no cartão em três vezes ou mais, preço normal do produto mais juros de 10%')
opção = int(input('Digite sua opção: '))

if opção == 1:
    preço_final = preço - preço * 0.15
elif opção == 2:
    preço_final = preço - preço * 0.10
elif opção == 3:
    preço_final = preço
    parcela = preço / 2
    print(f'Seu valor será parcelado em 2 vezes de R$ {parcela:.2f}')
elif opção == 4:
    preço_final = preço + preço * 0.10
    parcelas = int(input('Quantas parcelas? '))
    parcela = preço_final / parcelas
    print(f'Seu valor será parcelado em {parcelas} vezes de R$ {parcela:.2f}')
else:
    print('Opção inválida. Por favor, escolha uma opção válida.')  

if opção in [1,2,3,4]:
    print(f'O valor final do produto a ser pago é: R$ {preço_final:.2f}')   