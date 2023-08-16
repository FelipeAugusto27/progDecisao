'''
Fzer um algorítimo que pergunte o ano de nascimento de uma pessoa e o ano atual. Ao final, o algorítimo deverá na tela
a idade da pessoa. Porém, se o usuário inserir o ano de nascimento com valor maior do que o ano atual, o cálculo da
idade não deverá ser feito, e então deverá surgir a seguinte mensagem na tela: "Dados inseridos estão incorretos".
'''

# Input
nasc = int(input("Informe o ano de nascimento: "))
ano = int(input("Informe o ano atual: "))

# Processamento
idade = ano - nasc
resposta = "Dados inseridos estão incorretos." if nasc > ano else f"Você tem {idade} anos de idade."

# Output
print(resposta)
