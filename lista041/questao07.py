'''
Desenvolver um programa que pergunte um valor inteiro e positivo ou negativo, exiba a resposta como módulo deste valor,
ou seja, o número lido como positivo.
'''

# Input
num = int(input("Informe um número: "))

# Processamento e Output
if (num > 0):
    print(f"O módulo do valor é {num}")
else:
    print(f"O módulo do valor é {-num}")
