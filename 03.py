#Entrada do usuário
nome1 = str(input("Digite o nome da 1º pessoa: "))
idade1 = float(input("Digite a idade da 1º pessoa: "))
nome2 = str(input("Digite o nome da 2º pessoa: "))
idade2 = float(input("Digite a idade da segunda pessoa: "))

#Calculadora
ano_atual = 2023
nascimento1 = ano_atual - idade1
nascimento2 = ano_atual - idade2

#Condicionais
if (idade2 < idade1):
    print(nome2, " é a pessoa mais nova, pois ela nasceu em: ", nascimento2)
elif (idade1 < idade2):
    print(nome1, " é a pessoa mais nova, pois ela nasceu em: ", nascimento1)
else:
    print("As duas pessoas tem a mesma idade, ambas nasceram em ", nascimento1)