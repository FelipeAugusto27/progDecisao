'''
Desenvolver um programa que pergunte um número e exiba a informação de que ele é positivo, negativo ou nulo.
'''

# Input
num = float(input("Informe um número: "))

# Processamento e Output
if num > 0:
    print("O número é positivo.")
elif num < 0:
    print("O número é negativo.")
else:
    print("O número é nulo.")
