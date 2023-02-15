#Entrada usuário
nome = str(input("Digite o nome do aluno: "))
nota1 = float(input("Digite a 1º nota do aluno (0 a 10): "))
nota2 = float(input("Digite a 2º nota do aluno (0 a 10):"))
 
#Calculos matemáticos
media_aluno = (nota1 + nota2) / 2
media_reprovado = 5
media_geral = 7

#Condições
if (media_aluno < media_reprovado):
    print("Reprovado")
elif (media_aluno < media_geral):
    print("Recuperação")
else:
    print("Aprovado")