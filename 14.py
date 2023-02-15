#Entrada usuário
tipo = str(input("Digite o qual seu tipo de consumidor (I, C ou R): "))
consumo = float(input("Digite qual foi o seu consumo mensal: "))
c1 = "I"
c2 = "C"
c3 = "R"

#Condições
if (tipo == c1):
    valor = (0.68 * consumo) + 34
    print("O valor da conta mensal de energia é R$", valor)
elif (tipo == c2):
    valor = (0.37 * consumo) + 45
    print("O valor da conta mensal de energia é R$", valor)
elif (tipo == c3):
    valor = (0.77 * consumo) - 22
    print("O valor da conta mensal de energia é R$", valor)