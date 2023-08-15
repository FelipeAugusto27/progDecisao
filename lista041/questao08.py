'''
Desenvolver um programa que pergunte um número inteiro qualquer e verifique se ele está na faixa de 1 a 10
'''

# Input
num = int(input("Informe um número: "))

# Processamento e Output
if (num > 0) and (num < 11):
    print(f"{num} está entre 1 e 10.")
else:
    print(f"{num} não está entre 1 e 10")
