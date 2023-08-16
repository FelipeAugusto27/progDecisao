'''
Fazer um algorítimo que peça um número, e ao final, informe se o número digitado está acima de 1000 ou abaixo de 1000
'''

# Input
num = int(input("Informe um número: "))

# Processamento
resposta = "O número é maior que 1000." if num > 1000 else "O número está abaixo de 1000." if num < 1000 else "O número é 1000."

# Output
print(resposta)
