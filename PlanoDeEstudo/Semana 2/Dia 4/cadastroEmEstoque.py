#Pograma de cadastro em estoque

#Cria lista princípal
estoque = []

#Função que cadastra produto e adiciona a lista principal
def cadastrar_produto(nome, preco, quantidade):
    produto = { #Dicionário com dados cadastrados
        "nome": nome,
        "preco": preco,
        "quantidade": quantidade
    }
    estoque.append(produto)

#Função para exibir lista principal percorrendo ela e exibindo cada dado
def listar_produtos(estoque):
    for produtos in estoque:
        print(f"Nome: {produtos['nome']}")
        print(f"Preço: {produtos['preco']}")
        print(f"Quantidade: {produtos['quantidade']}")


#Menu interativo com loop while
while True:
    #Pede ao usuário que diga o que quer fazer
    print("\n=== Cadastro de Produtos ===")
    print("Digite '1' para começar a cadastrar")
    print("Digite '2' para listar os itens no estoque")
    print("Digite '0' para finalizar o programa")

    #Recebe informação do usuário da operação que quer executar
    start = int(input("\nO que deseja fazer? "))

    #Estrutura condicional para pegar instrução do usuário e executar de acordo comsua função
    if  start == 1:
       nome_produto = input("\nDigite o nome do produto: ")
       preco_produto = float(input("Digite o preço do produto: "))
       quantidade_produto = int(input("Digite a quantidade do produto: "))
        #Chama a função que irá receber os dados do usuário e adiciona a lista principal de estoque
       cadastrar_produto(nome_produto, preco_produto, quantidade_produto)

    elif start == 2:
        listar_produtos(estoque) #Exibe a lista principal, com os produtos cadastrados pelo usuário

    elif start == 0:
        print("Finalizando Cadastro...")
        break #Quebra o loop e finaliza o programa
    #Evita instruções diferentes das sugeridas
    else:
        print("Inválido!")
