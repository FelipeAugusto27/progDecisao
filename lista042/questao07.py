'''
Fazer um algorímito que pergunte 2 números, e ao final, exiba como resposta na tela qual é o maior e o menor, ou ainda,
se ambos são iguais
'''

# Input
num1 = int(input("Informe um primeiro número: "))
num2 = int(input("Informe um segundo número: "))

# Processamento
resposta = f"{num1} é maior do que {num2}" if num1 > num2 else f"{num2} é maior do que {num1}" if num1 < num2 else "Os números tem o mesmo valor"

# Output
print(resposta)
