#Prática de estrutura de dados

#Primeiro exercicio
#Programa que recebe dados e exibe a quantidade de cada elemento

#Recebe as frutas em sua quantidade
frutas = input("Digite cada fruta dispoível em sua qauntidade: ").split()

#Dicionário vazio para criação com as frutas e suas quantidade
contagem = {}

#Laço que verifica a quantidade e adiciona ao dicionário caso não esteja e adiciona mais 1 caso esteja
for fruta in frutas:
    if fruta in contagem:
        contagem[fruta] = contagem[fruta] + 1
    else:
        contagem[fruta] = 1

#Retorna o dicionário criado
print(contagem)