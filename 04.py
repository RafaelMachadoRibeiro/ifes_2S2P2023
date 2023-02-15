#Entrada usuario
num1 = float(input("Digite o 1º número: "))
num2 = float(input("Digite o 2º número: "))
num3 = float(input("Digite o 3º número: "))

#Condicionais
if (num1 > num2 and num1 > num3):
    print(num1, " é maior que todos os números")
elif (num2 > num1 and num2 > num3):
    print(num2, " é maior que todos os números")
elif (num3 > num1 and num3 > num2):
    print(num3, " é maior que todos os números")
