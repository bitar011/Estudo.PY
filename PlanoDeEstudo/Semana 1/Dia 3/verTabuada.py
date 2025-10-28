#Programa que vai retornar a tabuada de um número

#Recebe o número que quer ver a tabuada
num = int(input("Digite o número que quer ver a tabuada: "))

#Retorna mensagem
print(f"Tabuada do {num}")
#Gera a sequencia em que i recebe cada valor(menos o último), a cada volta do laço
for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")