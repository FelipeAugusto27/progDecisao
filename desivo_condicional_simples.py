'''
Crie um programa que pergunte dois números ao usuário
em seguida o programa deverá somar os dois e apresentar o resultado se o valor da soma for maior do que 10
'''

# Input
num1 = int(input("Informe um primeiro número: "))
num2 = int(input("Informe um segundo número: "))

# Processamento
soma = num1 + num2

# Output
if (soma > 10):
    print(f"A soma dos números é maior que 10: {soma}")

print("FIM")