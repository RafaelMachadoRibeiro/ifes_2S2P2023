#Interação com o usuário
mes = str(input("Digite o número do mês: "))
ano = float(input("Digite o ano: "))

#Ano bissexto
if (ano%4==0 and ano%100!=0) or (ano%400==0):
    if mes in ["1", "3", "5", "7", "8", "10", "12"]:
        print("31 dias")
    elif mes in ["4", "6", "9", "11"]:
        print("30 dias")
    elif (mes == "2"):
        print("29 dias")

#Ano normal
else:
    if mes in ["1", "3", "5", "7", "8", "10", "12"]:
        print("31 dias")
    elif mes in ["4", "6", "9", "11"]:
        print("30 dias")
    elif (mes == "2"):
        print("28 dias")
