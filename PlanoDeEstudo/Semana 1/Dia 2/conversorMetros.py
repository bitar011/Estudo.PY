#Convertendo com i/o, variáveis e condições
metros = float(input("Digite o valor que deseja converter em metros: "))
medida = input("Digite a medida que deseja(cm, mm): ")

if medida == "cm":
    valor = metros * 100
elif medida == "mm":
    valor = metros * 1000
else:
    valor = "Medida indisponível"

print(valor)