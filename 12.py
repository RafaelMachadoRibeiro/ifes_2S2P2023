#Entrada usuário
sexo = str(input("Digite o seu sexo (H ou M): "))
idade = float(input("Digite a sua idade: "))
sex1 = "H" 
sex2 = "M" 

#Condicionais
if (sexo == sex1 and idade > 21):
    idade = "21"
    print("A idade é: ", idade)
elif (sexo == sex2 and idade > 18):
    idade = "18"
    print("A idade é: ", idade)
else:
    print ("A idade é: ", idade)

