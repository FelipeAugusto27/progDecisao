'''
Desenvolver um programa que pergunte um número inteiro e faça a exibição desse valor caso seja divisível por 5.
Não sendo divisível por 4 e 5, o programa deverá exibir a mensagem "Valor não é divisível por 4 e 5".
'''

# Input
num = int(input("Informe um número inteiro: "))

# Processamento e Output
if (num%4 == 0) and (num%5 == 0):
    print(f"{num} é divisível por 4 e 5")
else:
    print("Valor não é divisível por 4 e 5 simultaneamente")
