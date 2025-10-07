#Verificação de estrutura

#Função definida para verificar a estrutura
def verificar_balanceamento(simbolos):
    #Cria pilha vazia
    pilha = []
    #Dicionário de pares
    pares = {')': '(', '}': '{'}

    #Verifica se é par ou ímpar para dizer se estar balanceada ou não
    for s in simbolos:
        if s in '({':
            pilha.append(s)
        elif s in ')}':
            if not pilha or pilha[-1] != pares[s]:
                return False
            pilha.pop()

    return len(pilha) == 0


#Programa interativo
print("=== Verificador de Balanceamento de Símbolos ===")

#Loop para interatividade de saída
while True:
    #Recebe a expressão
    expressao = input("\nDigite uma expressão (ou 'sair' para encerrar): ")

    #Chama a função para verificar e retornar a resposta
    if expressao.lower() == 'sair':
        print("Encerrando o programa... ")
        break

    if verificar_balanceamento(expressao):
        print("A expressão está balanceada!")
    else:
        print("A expressão está desbalanceada.")
