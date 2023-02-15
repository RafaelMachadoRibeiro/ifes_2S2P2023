#Entrada usuário
angulo1 = float(input("Digite o 1º angulo do triângulo: "))
angulo2 = float(input("Digite o 2º angulo do triângulo: "))
angulo3 = float(input("Digite o 3º angulo do triângulo: "))

#Matemática
cond_tri = angulo1 + angulo2 + angulo3

#Condicionais
if(cond_tri > 180):
    print("Não é possível formar um triângulo.")

elif (angulo1 > 90 or angulo2 > 90 or angulo3 > 90):
    print("É um triângulo obtusângulo")
elif (angulo1 == 90 or angulo2 == 90 or angulo3 == 90):
    print("É um triângulo retângulo")
elif (angulo1 < 90 or angulo2 < 90 or angulo3 < 90):
    print("É um triângulo acutângulo")