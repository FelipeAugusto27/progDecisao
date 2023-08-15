'''
Desenvolver um programa que pergunte um número inteiro de 3 algarismos e apresente somente o algarismo das centenas
'''

# Input
num = int(input("Informe o número de 3 digitos: "))

# Processamento e Output
if (num < 1000) and (num > 99):
    print(f"O terceiro algarismo de {num} é {num // 100}")
else:
    print("O número informado é invalido.")
