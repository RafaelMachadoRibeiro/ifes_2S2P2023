#Entrada usuário
nome_aluno = str(input("Digite o nome do aluno: "))
media_aluno = float(input("Digite a média do aluno: "))
faltas_aluno = float(input("Digite o número de faltas do aluno: "))

#Condições
if (media_aluno >= 7 and faltas_aluno <= 32):
    print("Aprovado")
elif (media_aluno < 7 and faltas_aluno <= 32):
    print("Reprovado por média")
elif (media_aluno > 7 and faltas_aluno > 32):
    print("Reprovado por falta")
elif (media_aluno < 7 and faltas_aluno > 32):
    print("Reprovado por falta e média")       