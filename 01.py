#Entrada do usuário
valor_financeamento = float(input("Digite o valor que deseja financear: "))
valor_salario = float(input("Digite o seu salário: "))

#Calculos matemáticos
valor_maximo = valor_salario * 5

#Condicionais
if (valor_financeamento <= valor_maximo):
    print("Financiamento Concedido")
else:
    print("Fincanciamento Negado")

#Frase final
print("Obrigado por nos consultar.")