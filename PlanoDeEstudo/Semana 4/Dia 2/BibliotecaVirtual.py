#Programa de biblioteca virtual,
#utilizando funções e manipulando arquivos

import json

#Lista principal com as informações dos livros na biblioteca
biblioteca = []

#Função que cadastra livro
def cadastrar_livro(titulo, autor, editora):
    livro = {
        "titulo": titulo,
        "autor": autor,
        "editora": editora,
        "disponivel": True
        }
    biblioteca.append(livro)
    return f"Livro adicionado com sucesso!"

#Função para listar livros na biblioteca
def listar_livros():
    print("--- Livros na Biblioteca ---")
    #Verifica se a biblioteca está vazia
    if not biblioteca:
        print("Nenhum livro cadastrado ainda.")
        return
    #Se não estiver, percorre a lista, verifica status e exibe os titulos e seus status
    for livro in biblioteca:
        if livro["disponivel"] == True:
            status = ("Disponível!")
        else:
            status = ("Indisponível.")

        print(f"{livro['titulo']} {status}")
    print("----------------------------")

#Função para emprestar livros
def emprestar_livro(titulo_busca):
    #Percorre a biblioteca
    for livro in biblioteca:
        #Encontra o livro pelo título
        if livro["titulo"] == titulo_busca:
            
            #Verifica se está disponível
            if livro["disponivel"] == True:
                #Muda o status para False
                livro["disponivel"] = False
                print(f"O livro '{titulo_busca}' foi emprestado com sucesso!")
            else:
                #Se 'disponivel' já era False
                print(f"Desculpe, o livro '{titulo_busca}' já está emprestado.")
                
            return #Achamos o livro (emprestado ou não), então paramos a função
            
    #Se o loop terminar (não achou o livro):
    print(f"O livro '{titulo_busca}' não foi encontrado na biblioteca.")

#Funçao para devolver livro
def devolver_livro(titulo_busca):   
    #Percorre a biblioteca
    for livro in biblioteca:
        #Encontra o livro
        if livro["titulo"] == titulo_busca:
            
            #Verifica se está indisponível
            if livro["disponivel"] == False:
                #Muda o status para True
                livro["disponivel"] = True
                print(f"O livro '{titulo_busca}' foi devolvido com sucesso! ⬅️")
            else:
                #Se 'disponivel' já era True
                print(f"Opa, o livro '{titulo_busca}' já consta como disponível.")
                
            return #Achamos o livro (devolvido ou não), paramos a função
            
    #Se o loop terminar (não achou):
    print(f"O livro '{titulo_busca}' não foi encontrado na biblioteca.")

#Função para salvar os dados em um arquivo
def salvar_dados():
    # 1. Abrimos o arquivo em modo "w" (escrita)
    with open("biblioteca.json", "w") as f:
        # 2. Usamos json.dump para salvar nossa lista lá dentro
        json.dump(biblioteca, f, indent=4) 
        
    print("Dados salvos com sucesso em 'biblioteca.json'!")

#Função para carregar os dados
def carregar_dados():
    global biblioteca #Aviso que vamos alterar a variável 'global'
    try:
        #Abre no modo leitura (r)
        with open("biblioteca.json", "r") as f:
            #Carrega os dados do arquivo para a variável
            biblioteca = json.load(f)
        print("Dados carregados com sucesso! 📚")
    except FileNotFoundError:
        #Se o arquivo não existir, apenas avisamos.
        print("Arquivo 'biblioteca.json' não encontrado. Começando com uma biblioteca vazia.")
    except json.JSONDecodeError:
        #Se o arquivo estiver vazio ou corrompido
        print("Erro ao ler o arquivo JSON. Começando com uma biblioteca vazia.")

#Menu de interativdade com o usuário
while True:
    print("==== BIBLIOTECA VIRTUAL ====")
    print("Digite '1' para cadastrar um livro.")
    print("Digite '2' para listar livros da biblioteca.")
    print("Digite '3' para pegar um livro emprestado.")
    print("Digite '4' para devolver livro emprestado.")
    print("==============================")

    escolha = int(input("Digite sua escolha: "))
