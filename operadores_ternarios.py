'''
Crie um programa que pergunte a idade do usuário e em seguida informe se o usuário é maior ou menor de idade
'''
#Lógica do ternário1: variavel = (se for falso, se for verdadeiro)[teste condicional]

# Input
idade = int(input("Informe a sua idade: "))

# Processamento e Output
resposta = ("Você é menor de idade", "Você é maior de idade")[idade>=18]
print(resposta)
