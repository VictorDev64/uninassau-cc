#Faça um algoritmo que leia dois valores booleanos (lógicos) e determine se ambos são VERDADEIRO ou FALSO, 
#sendo o numero 1 Verdadeiro e 0 Falso.

valor1 = int(input("Digite o primeiro valor (1 ou 0): "))
valor2 = int(input("Digite o segundo valor: (1 ou 0): "))

verdadeiro1 = bool(valor1)
verdadeiro2 = bool(valor2)

if verdadeiro1 and verdadeiro2: 
    print("Ambos os valores são Verdadeiro.")
elif not verdadeiro1 and not verdadeiro2:
    print("Ambos os valores são Falso.")
else:
    print("Os valores são diferentes (um é Verdadeiro e o outro é Falso).") 