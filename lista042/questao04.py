'''
Fazer um algorítimo que peça um número, de 1 a 7 e ao final, informe o dia da semana (por extenso) correspondente
ao número que foi inserido. Informar também a mensagem "número inválido" quando o número não corresponder à um dia da semana
'''

# Input
num = int(input("Informe um número de 1 a 7: "))

# Processamento
resposta = "Domingo" if num == 1 else "Segunda-Feira" if num == 2 else "Terça-Feira" if num == 3 else "Quarta-Feira" if num == 4 else "Quinta-Feira" if num == 5 else "Sexta-Feira" if num == 6 else "Sabado" if num == 7 else "Número Inválido"

# Output
print(resposta)
