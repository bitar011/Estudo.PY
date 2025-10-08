#Otimizador de estrutura

#Função para otimizar, recebendo listas e retornando a interseção entre elas
def intersecao_otimizada(lista_a, lista_b):
    set_a = set(lista_a)
    set_b = set(lista_b)
    return list(set_a & set_b)

#Parte interativa com usuário
print("=== Interseção de Listas ===")
#Recebe as listas
lista_a = list(map(int, input("Digite os números da lista A (separados por espaço): ").split()))
lista_b = list(map(int, input("Digite os números da lista B (separados por espaço): ").split()))

#Chama a função
resultado = intersecao_otimizada(lista_a, lista_b)

#Retorna a função exibindo o resultado
print("\nElementos comuns (sem duplicatas):", resultado)
