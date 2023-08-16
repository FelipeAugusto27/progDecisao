'''
Fazer um algorítimo que peça um número, e ao final, informe se o número digitado está abaixo de 1000, entre 1000 e 5000, entre 5001 e 8000, ou acima de 8000.
'''

# -1000, 1000-5000, 5001-8000, +8000

# Input
num = int(input("Informe um número: "))

# Processamento
resposta = "O número é menor que 1000" if num < 1000 else "O número está entre 1000 e 5000" if num <= 5000 else "O número está entre 5001 e 8000" if num <= 8000 else "O número é maior que 8000"

# Output
print(resposta)
