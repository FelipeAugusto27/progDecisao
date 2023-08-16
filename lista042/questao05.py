'''
Fazer um algorítimo que pergunte a sigla de um estado do (UF -> Unidade Federativa), e ao final, informe na tela se o estado inserido está ou não no Sudeste
'''

# Input
uf = input("Informe uma UF (Por favor, escrever a sigla em maiusculo: ")

# Processamento
resposta = f"{uf} pertence a região Sudeste" if uf == "RJ" or uf == "MG" or uf == "SP" or uf == "ES" else "O estado não pertence a região sudeste ou foi escrito incorretamente."

# Output
print(resposta)
