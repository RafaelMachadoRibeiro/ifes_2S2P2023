#Entrada do usuário
tempo_carro1 = float(input("Digite o tempo do carro_1 na pista: "))
tempo_carro2 = float(input("Digite o tempo do carro_2 na pista: "))
distancia_carro1 = float(input("Digite a distância percorrida pelo carro_1 na pista: "))
distancia_carro2 = float(input("Digite a distância percorrida pelo carro_2 na pista: "))

#Calculos matemática
velocidade_media1 = distancia_carro1 / tempo_carro1
velocidade_media2 = distancia_carro2 / tempo_carro2

#Condicionais
if (velocidade_media2 < velocidade_media1):
    print("O carro_1 é mais rápido que o carro_2.")
elif (velocidade_media1 < velocidade_media2):
    print("O carro_2 é mais rápido que o carro_1.")
else:
    print("A velocidade dos carro são iguais.")