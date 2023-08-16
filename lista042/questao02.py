'''
Fazer um algorítimo que peça um número, e ao final, informe se o número digitado está abaixo de 1000, entre 1000 e 5000,
ou acima de 5000
'''

# Input
num = int(input("Informe um número: "))

# Processamento
resposta = "O número está abaixo de 1000" if num < 1000 else "O número está acima de 5000" if num > 5000 else "O número está entre 1000 e 5000"

# Output
print(resposta)
