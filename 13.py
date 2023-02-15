#Entradas do usuário
qnt_aco = float(input("Digite quantas hastes de aço quer comprar: "))
qnt_cob = float(input("Digite quantas hastes de cobre deseja comprar: "))
qnt_alu = float(input("Digite quantas hastes de aluminio deseja comprar: "))

#Calculos matemáticos
valor_aco = qnt_aco * 2.5
valor_cob = qnt_cob * 4.0
valor_alu = qnt_alu * 5.0
qnt_ttl = qnt_aco + qnt_cob + qnt_alu

#Condicionais
if (qnt_ttl < 6):
    valor_total = (valor_cob * 1) + (valor_alu * 1) + (valor_aco * 1)
    print("O valor total da compra deu R$", valor_total)
elif (qnt_ttl <= 15):
    valor_total = (valor_cob * 0.9) + (valor_alu * 0.9) + (valor_aco * 0.9)
    print("O valor total da compra deu R$", valor_total)
elif (qnt_ttl <= 20):
    valor_total = (valor_cob * 0.85) + (valor_alu * 0.85) + (valor_aco * 0.85)
    print("O valor total da compra deu R$", valor_total)
elif (qnt_ttl > 20):
    valor_total = (valor_cob * 0.80) + (valor_alu * 0.80) + (valor_aco * 0.80)
    print("O valor total da compra deu R$", valor_total)