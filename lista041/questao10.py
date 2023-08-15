'''
Desenvolver um programa que pergunte dois números inteiros, e apresente como resultado se o segundo número informado é
ou não divisor do primeiro
'''

# Input
num1 = int(input("Informe um primeiro número: "))
num2 = int(input("Informe um segundo número: "))

# Processamento e Output
if (num1%num2 == 0):
    print(f"{num2} é divisor de {num1}")
else:
    print(f"{num2} não é divisor de {num1}")
