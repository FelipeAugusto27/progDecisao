'''
Fazer um algorítimo que pergunte o nome do aluno, e as notas das provas 1 e 2. Deverá exibir na tela como resposta a
média do aluno, e se ele está aprovado, reprovado, ou em prova final. Estas condições devem seguir as regras da tabela

Média    Situação
-3,0   |Reprovado
3,0-6,9|Prova final
>=7,0  |Aprovado
'''

# Input
nome = input("Informe seu nome: ")
nota1 = float(input("Informe a primeira nota: "))
nota2 = float(input("Informe a segunda nota: "))

# Processamento
media = (nota1 + nota2) / 2
if media < 3:
    condicao = "Reprovado"
elif media >= 7:
    condicao = "Aprovado"
else:
    condicao = "Prova final"
#Output
print(f"Nome: {nome}")
print(f"Média: {media}")
print(f"Condição: {condicao}")