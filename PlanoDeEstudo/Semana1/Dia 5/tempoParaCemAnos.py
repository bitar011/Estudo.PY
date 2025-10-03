#Calcula em quanto tempo e o ano a pessoa terá 100 anos

#Recebe nome e idade
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
#Ano atual
ano_atual = 2025

#Calcula quantos anos faltam e o ano de completar os 100
cem_anos = 100 - idade
ano_final = ano_atual + cem_anos


print(f"{nome}, em {cem_anos} anos você terá 100 anos.")
print(f"Você fará 100 anos em {ano_final}.")