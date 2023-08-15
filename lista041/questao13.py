'''
Desenvolver um programa que pergunte 3 valores (a, b, c) e ao final e apresente-os dispostos em ordem crescente
'''

# Input
a = int(input("Informe um primeiro valor: "))
b = int(input("Informe um primeiro valor: "))
c = int(input("Informe um primeiro valor: "))

# Processamento
# Tornando a menor que b
if (a>b):
    z = a
    a = b
    b = z
# a < b agora

# Tornando a menor que o c
if (a > c):
    z = a
    a = c
    c = z
# a < c agora

# Tornando b menor que o c
if (b > c):
    z = b
    b = c
    c = z
# b < c agora

print(f" a ordem crescente é: {a, b, c}")