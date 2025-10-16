#Programa que gera senhas aleátorias de acordo com escolhas do usuário

#Importa biblioteca para ajudar na manipulação
import random as rd

#Define listas usadas para confecção de senhas
letras_minusculas = "abcdefghijklmnopqrstuvwxyz"
letras_maiusculas = letras_minusculas.upper()
numeros = "0123456789"
simbolos = "_*$#@"

#Recebe as escolhas do usuário
comprimento = int(input("Digite o comprimento que deseja(max. 16): "))
qtde_numeros = int(input("Digite a quantidade de números que deseja: "))
qtde_simbolos = int(input("Digite a quantidade de símbolos que deseja: "))

#Calcula e define total de letas com base nas escolhas de numeros e simbolos do usuário
qtde_letras = comprimento - (qtde_numeros + qtde_simbolos)

#Cria lista de todas as letras disponíveis 
todas_as_letras = letras_maiusculas + letras_minusculas

#Lista principal que irá armazenar a senha
senha_lista = []

#Loops que percorrem e escolhem aleatoriamente os caracteres que estarão na senha finaçl
for n in range(qtde_numeros):
    qtde_numeros_senha = rd.choice(numeros)
    senha_lista.append(qtde_numeros_senha)

for n in range(qtde_simbolos):
    qtde_simbolos_senha = rd.choice(simbolos)
    senha_lista.append(qtde_simbolos_senha)

for n in range(qtde_letras):
    qtde_letras_senha = rd.choice(todas_as_letras)
    senha_lista.append(qtde_letras_senha)

#Embaralha itens na lista
rd.shuffle(senha_lista)

#Exibe senha final toda junta, sem separação
print("".join(senha_lista))

#Próximo passo, refatorar usando funções