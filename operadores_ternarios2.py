'''
Crie um programa que pergunte a idade do usuário e em seguida informe se o usuário é maior ou menor de idade
'''
#Lógica do ternário1: variavel = resultado_verdadeiro if teste_condicional else resultado falso

# Input
idade = int(input("Informe a sua idade: "))

# Processamento e Output
resposta = "Você é maior de idade" if idade >= 18 else "Você é menor de idade"

print(resposta)