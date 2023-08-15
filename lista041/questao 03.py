'''
Desenvolver um programa que pergunte um número, e apresente como resposta se o referido número for par ou ímpar.
'''

# Input
num = int(input("Informe um número: "))

# Processamento e Output
if (num%2) == 0:
    print(f"{num} é par")
else:
    print(f"{num} é ímpar")
