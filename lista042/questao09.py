'''
Fazer um algorítimo que pergunte a idade de uma pessoa, e ao final, informe se a pessoa é menor de idade, se é maior de
idade, ou se é maior de 65 anos
'''

# Input
idade = int(input("Informe a sua idade: "))

# Processamento
resposta = "Você é menor de idade." if idade < 18 else "Você é maior de 65 anos." if idade > 65 else "Você é maior de idade"

# Output
print(resposta)