'''
Desenvolver um programa que pergunte 4 notas escolares de um aluno exiba a mensagem informando que o aluno foi aprovado
se a média escolar for maior ou igual a 5. Se o aluno não foi aprovado, indicar uma mensagem
'''

# Input
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))
nota3 = float(input("Informe a terceira nota: "))
nota4 = float(input("Informe a quarta nota: "))

# Processamento e Output

media = (nota1 + nota2 + nota3 + nota4)/4

if media > 4:
    print(f"Sua média de {media}, você foi aprovado")
else:
    print(f"Sua média de {media}, você não foi aprovado")