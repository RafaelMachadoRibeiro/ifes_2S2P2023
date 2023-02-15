#Entrada do usuário
salario = float(input("Digite o seu salário bruto: "))

#Condições
if (salario < 1903.98):
    print("Você é insento de imposto de renda.")

elif (salario < 2826.65):
    imposto = (salario * 0.075) - 142.8
    salario_liquido = salario - imposto
    print("O seu salário líquido será R$", salario_liquido)

elif (salario < 3751.05):
    imposto = (salario * 0.15) - 548.82
    salario_liquido = salario - imposto
    print("O seu salário líquido será R$", salario_liquido)

elif (salario < 4664.68):
    imposto = (salario * 0.225) - 636.13
    salario_liquido = salario - imposto
    print("O seu salário líquido será R$", salario_liquido)
    
elif (salario > 4664.68):
    imposto = (salario * 0.275) - 869.36
    salario_liquido = salario - imposto
    print("O seu salário líquido será R$", salario_liquido)