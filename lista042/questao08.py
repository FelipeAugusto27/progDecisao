'''
Fazer um algorítimo que pergunte 3 números, e ao final guarde na variável 'maior', o maior destes 3 números inseridos.
O valor da variavel 'maior' deverá ser exibido no final.
'''

# Input
num1 = int(input("Informe o primeiro número: "))
num2 = int(input("Informe o segundo número: "))
num3 = int(input("Informe o terceiro número: "))

# Processamento
maior = num1
if maior < num2:
    maior = num2
if maior < num3:
    maior = num3

# Output
print(f"O maior valor é de {maior}")
