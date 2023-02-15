#Entrada usuário
km = float(input("Digite os kilometros rodados: "))
litro = float(input("Digite os litros gastos: "))
km_l = km / litro

#Condições
if (km_l < 8):
    print("Venda o carro!")
elif (km_l <= 12):
    print("Econômico!")
elif (km_l > 12):
    print("Super econômico!")
