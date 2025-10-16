#Refatoração do gerador de senhas, utilizando funções e adicionando interatividade

#Importação de módulos(prática da semana)
import random as rd
import string #Uma dica para simplificar a criação dos caracteres

#DEFINIÇÃO DOS CARACTERES
#Usando o módulo string, fica mais fácil e menos sujeito a erros
letras_minusculas = string.ascii_lowercase
letras_maiusculas = string.ascii_uppercase
numeros = string.digits
simbolos = "@#$%*_"
todas_as_letras = letras_minusculas + letras_maiusculas

#Função principal
def gerar_senha(comprimento, qtde_numeros, qtde_simbolos):
    """Gera uma senha aleatória com base nos parâmetros fornecidos."""
    
    #1. Calcular a quantidade de letras
    qtde_letras = comprimento - (qtde_numeros + qtde_simbolos)
    
    senha_lista = []

    #2. Sortear os caracteres
    for _ in range(qtde_numeros):
        senha_lista.append(rd.choice(numeros))

    for _ in range(qtde_simbolos):
        senha_lista.append(rd.choice(simbolos))

    for _ in range(qtde_letras):
        senha_lista.append(rd.choice(todas_as_letras))

    #3. Embaralhar e juntar
    rd.shuffle(senha_lista)
    senha_final = "".join(senha_lista)
    
    #4. Retornar o resultado
    return senha_final

#Loop principal (Interação com o usuário)
while True:
    try:
        print("--- Gerador de Senhas ---")
        comprimento = int(input("Digite o comprimento total da senha(max. 16): "))
        qtde_numeros = int(input("Digite a quantidade de números: "))
        qtde_simbolos = int(input("Digite a quantidade de símbolos: "))

        #Validação
        if qtde_numeros + qtde_simbolos > comprimento:
            print("\n[ERRO] A soma de números e símbolos não pode exceder o comprimento total.\n")
            continue #Volta para o início do loop

        #Chamada da função
        senha_gerada = gerar_senha(comprimento, qtde_numeros, qtde_simbolos)
        print("\nSua senha segura é:", senha_gerada, "\n")

    except ValueError:
        print("\n[ERRO] Por favor, digite apenas números válidos.\n")
        continue

    #Perguntar se quer continuar
    resposta = input("Deseja gerar outra senha? (s/n): ")
    if resposta.lower() != 's':
        break #Encerra o loop while

print("Obrigado por usar o programa!")