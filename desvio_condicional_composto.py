'''
Crie um programa que pergunte a idade de uma pessoa
Em seguida o programa deve informar se a pessoa é menor de idade ou maior de idade.
'''

# Input
idade = int(input("Informe sua idade: "))

# Processamento
if (idade >= 18):
    print("Adulto(a)")
else:
    print("Menor")

print("FIM")