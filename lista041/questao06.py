'''
Desenvolva um programa que pergunte dois valores inteiros e apresente o valor da diferença entre o maior e o menor.
'''

# Input
num1 = int(input("Informe um número inteiro: "))
num2 = int(input("Informe outro número inteiro: "))

# Processamento e Output
if num1 > num2:
    print(f"O valor da diferença de {num1} e {num2} é de {num1-num2}")
else:
    print(f"O valor da diferença de {num2} e {num1} é de {num1-num2}")
