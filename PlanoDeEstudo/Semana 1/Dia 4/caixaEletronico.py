#Programa para imitar um caixa eletrônico

#Recebe o valor que deseja
valor = int(input("Digite quanto deseja sacar: "))
#Notass disponíveis
notas = [100, 50, 20, 10, 5, 2]

print("Notas necessárias: ")
#Percorre a lista para verificar quantas notas de cada valor serão necessárias
for nota in notas:
    qtd = valor // nota #Divisão inteira para ver quantas vezes cabem no valor
    valor %= nota #Verifica quanto falta
    if qtd > 0:
        print(f"{qtd} nota(s) de R${nota}")