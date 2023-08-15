'''
Desenvolver um programa que pergunte um número.
Se este número for maior que 20, então ele deverá exibir a metade desse número, senão, então ele deverá exibir o número
sem alterações.
'''

# Input
num = float(input("Informe um número: "))

# Processamento e Output
if (num > 20):
    print(f"O valor da metade de {num} é: {num/2}")
else:
    print(f"O valor do número é: {num}")
