'''
Crie um programa que pergunte um número ao usuário.
Em seguida o programa deve informar se o número inserido está abaixo de 100, entre 100 e 200 ou acima de 200.
'''

# Input
num = int(input("Informe um primeiro valor: "))

# Processamento e Output
if (num < 100):
    print(f"O número {num} é menor que 100")
else:
    if (num <= 200): # num >= 100 é desnecessário.
        print(f"O número {num} está entre 100 e 200")

    else:
        print(f"O número {num} está acima de 200")

print("FIM")
