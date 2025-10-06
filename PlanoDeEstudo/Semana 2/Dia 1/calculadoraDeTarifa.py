#Calculadora de tarifas de estacionamento

#Recebe o tempo quue o usuário ficou
tempo = float(input("Digite o tempo que utilizou o espaço: "))

#Verifica o tempo e retorna o valor a pagar
if tempo < 1:
    print("Valor a pagar: R$5,00")
elif tempo >= 1 and tempo < 3:
    print("Valor a pagar: R$10,00")
elif tempo >= 3 and tempo < 6:
    print("Valor a pagar: R$15,00")
else:
    print("Valor a pagar: R$20,00")