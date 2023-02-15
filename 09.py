#Entrada do usuário
sexo = str(input("Digite o seu sexo: (M ou H): "))
peso = float(input("Digite o seu peso: "))
altura = float(input("Digite sua altura (CM): "))
idade = float(input("Digite sua idade: "))
sex1 = "H"
sex2 = "M"

#Condições
if (sexo == sex1):
    calorias = 66 + (13.7 * peso) + (5 * altura) - (6.8 * idade)
    print("Sua necessidade de calorias diárias é de: ", calorias)
elif (sexo == sex2):
    calorias = 665 + (9.6 * peso) + (1.8 * altura) - (4.7 * idade)
    print("Sua quantidade de calorias diárias necessárias é de: ", calorias)