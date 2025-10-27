#Melhorando o programa de biblioteca virtual, utilizando funções e manipulando arquivos
#Adicionando novas funcionalidades aprimorando a lógica do sistema

import json
import datetime

#Lista principal com as informações dos livros na biblioteca
biblioteca = []
#Lista com usuários cadastrados
usuarios = []

#Função que cadastra livro
def cadastrar_livro(titulo, autor, editora):
    livro = {
        "titulo": titulo,
        "autor": autor,
        "editora": editora,
        "disponivel": True
        }
    biblioteca.append(livro)
    print(f"\nO livro '{titulo}' foi cadastrado com sucesso!")
    salvar_dados()

#Função para cadastrar usuário(nova)
def cadastrar_usuario(nome, endereco, cpf):
    usuario = {
        "nome": nome,
        "endereco": endereco,
        "cpf": cpf
        }
    usuarios.append(usuario)
    return f"Usuário cadastrado com sucesso!"

#Função para listar livros na biblioteca
def listar_livros():
    print("--- Livros na Biblioteca ---")
    #Verifica se a biblioteca está vazia
    if not biblioteca:
        print("Nenhum livro cadastrado ainda.")
        return
    #Se não estiver, percorre a lista, verifica status e exibe os titulos e seus status
    for livro in biblioteca:
        if livro["disponivel"]:
            status = "(Disponível)"
            print(f"-> {livro['titulo']} (Autor: {livro['autor']}) - {status}")
        else:
            #Pega o nome e a data (com um valor padrão caso não exista)
            nome_usuario = livro.get("emprestado_para_nome", "Usuário Desconhecido")
            data_emprestimo = livro.get("data_emprestimo", "Data Desconhecida")
            
            status = f"(Emprestado para: {nome_usuario} em {data_emprestimo})"
            print(f"-> {livro['titulo']} (Autor: {livro['autor']}) - {status}")

#Função para listar usuários cadastrados
def listar_usuarios():
    """Mostra todos os usuários cadastrados."""
    print("\n---Usuários Cadastrados---")
    
    if not usuarios: #Verifica se a lista está vazia
        print("Nenhum usuário cadastrado ainda.")
        return

    # Loop que você criou:
    for usuario in usuarios:
        print(f"Nome: {usuario['nome']}")
        print(f"CPF:  {usuario['cpf']}")
        print("--------------------")

#Função para emprestar livros
def emprestar_livro(titulo_busca):
    """
    (Função de emprestimo atualizada) Encontra um livro, verifica um usuário pelo CPF
    e registra o empréstimo para esse usuário.
    """
    
    #1. Encontra o livro
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo_busca.lower(): #Ignora maiúsculas
            
            #2. Verifica se o livro está disponível
            if livro["disponivel"]:
                
                #--- Início da nova lógica de usuário ---
                
                #3. Pede o CPF para verificação
                cpf_busca = input(f"Livro '{livro['titulo']}' está disponível. Digite o CPF do usuário: ")
                
                #4. Procura o usuário na lista 'usuarios'
                usuario_encontrado = None # Começa assumindo que não achou
                for usuario in usuarios:
                    if usuario["cpf"] == cpf_busca:
                        usuario_encontrado = usuario #Caso achado, guardamos o dicionário dele.
                        break #Para o loop 'for usuario'
                
                #5. Verifica se o usuário foi encontrado
                if usuario_encontrado:
                    #Usuário existente. Finaliza o empréstimo.
                    
                    #Atualiza os dados do Livro
                    livro["disponivel"] = False
                    livro["emprestado_para_cpf"] = usuario_encontrado["cpf"]
                    livro["emprestado_para_nome"] = usuario_encontrado["nome"]
                    livro["data_emprestimo"] = str(datetime.date.today()) #Registra a data de hoje
                    
                    print(f"\nO livro '{livro['titulo']}' foi emprestado para {usuario_encontrado['nome']}!")
                    
                    #Salva TODAS as mudanças(no biblioteca.json)
                    salvar_dados() 
                    
                else:
                    #Usuário inexistente.
                    print(f"\nUsuário com CPF {cpf_busca} não foi encontrado no sistema.")
                    resposta = input("Deseja cadastrar este novo usuário agora? (s/n): ")
                    
                    if resposta.lower() == 's':
                        #Pede os dados que faltam para o cadastro
                        nome = input("Digite o nome do novo usuário: ")
                        endereco = input("Digite o endereço: ")
                        
                        #Chama a função de cadastro (passando o cpf que já temos)
                        cadastrar_usuario(nome, endereco, cpf_busca)
                        #(cadastrar_usuario já chama salvar_dados() para os usuários)
                        
                        #Avisa para tentar de novo, pois o empréstimo não foi finalizado.
                        print("\nUsuário cadastrado com sucesso. Por favor, repita a operação de empréstimo para finalizar.")
                    else:
                        print("\nEmpréstimo cancelado, pois o usuário não está cadastrado.")
                
                #--- Fim da lógica de usuário ---

            else:
                #Se o livro não estava disponível (disponivel == False)
                #Mostra para quem ele está emprestado, se tivermos a info
                quem_pegou = livro.get("emprestado_para_nome", "alguém")
                print(f"\nDesculpe, o livro '{livro['titulo']}' já está emprestado (com {quem_pegou}).")
            
            return #Sai da função (pois já tratamos este livro)
            
    #Se o loop terminar sem achar o livro
    print(f"\nO livro '{titulo_busca}' não foi encontrado na biblioteca.")
            
    #Se o loop terminar (não achou o livro):
    print(f"O livro '{titulo_busca}' não foi encontrado na biblioteca.")

#Funçao para devolver livro
def devolver_livro(titulo_busca):
    
    for livro in biblioteca:
        if livro["titulo"].lower() == titulo_busca.lower():
            
            #3. Verifica se está indisponível (False)
            if not livro["disponivel"]:
                
                #--- Início da nova lógica ---
                #Mudamos o status para True
                livro["disponivel"] = True
                
                #Limpamos os dados do empréstimo anterior
                livro["emprestado_para_cpf"] = ""
                livro["emprestado_para_nome"] = ""
                livro["data_emprestimo"] = ""
                #--- Fim da nova lógica ---

                print(f"O livro '{livro['titulo']}' foi devolvido com sucesso! ⬅️")
                salvar_dados() #Salva a mudança
            else:
                #Se 'disponivel' já era True
                print(f"\nOpa, o livro '{livro['titulo']}' já consta como disponível.")
                
            return #Achamos o livro (devolvido ou não), paramos a função
            
    #Se o loop terminar (não achou):
    print(f"\nO livro '{titulo_busca}' não foi encontrado na biblioteca.")


#Função para salvar os dados em um arquivo
def salvar_dados():
    #1: Salva os livros
    with open("biblioteca.json", "w") as f:
        json.dump(biblioteca, f, indent=4)
        
    #2: Salva os usuários(novo)
    with open("usuarios.json", "w") as f:
        json.dump(usuarios, f, indent=4)
        
    print("Dados (Livros e Usuários) salvos com sucesso! 💾")

#Função para carregar os dados
def carregar_dados():
    """Carrega Livros E Usuários dos arquivos JSON."""
    global biblioteca, usuarios #Avisa que vamos alterar as duas
    
    #1: Carrega os Livros
    try:
        with open("biblioteca.json", "r") as f:
            biblioteca = json.load(f)
        print("Dados da biblioteca carregados!")
    except FileNotFoundError:
        print("Arquivo 'biblioteca.json' não encontrado. Começando biblioteca vazia.")
    except json.JSONDecodeError:
        print("Erro ao ler 'biblioteca.json'. Começando biblioteca vazia.")

    #2: Carrega os Usuários(novo)
    try:
        with open("usuarios.json", "r") as f:
            usuarios = json.load(f)
        print("Dados de usuários carregados!")
    except FileNotFoundError:
        print("Arquivo 'usuarios.json' não encontrado. Começando com usuários vazios.")
    except json.JSONDecodeError:
        print("Erro ao ler 'usuarios.json'. Começando com usuários vazios.")



#Carrega dados alterados
carregar_dados() 

#Menu de interativdade com o usuário
while True:
    print("\n==== BIBLIOTECA VIRTUAL ====")
    print("1. Cadastrar Livro")
    print("2. Listar Livros")
    print("3. Emprestar Livro")
    print("4. Devolver Livro")
    print("5. Cadastrar Usuário")
    print("6. Listar Usuários")
    print("7. Sair")
    print("==============================")
    
    try:
        escolha = int(input("Digite sua escolha: "))
    except ValueError:
        print("\nErro: Por favor, digite apenas números.")
        continue

    #1. Cadastrar
    if escolha == 1:
        titulo = input("Digite o título: ")
        autor = input("Digite o autor: ")
        editora = input("Digite a editora: ")
        cadastrar_livro(titulo, autor, editora)

    #2. Listar
    elif escolha == 2:
        listar_livros()

    #3. Emprestar
    elif escolha == 3:
        titulo_busca = input("Digite o título do livro para emprestar: ")
        emprestar_livro(titulo_busca)

    #4. Devolver
    elif escolha == 4:
        titulo_busca = input("Digite o título do livro para devolver: ")
        devolver_livro(titulo_busca)

    elif escolha == 5:
        nome_user = input("Digite o nome: ")
        endereco_user = input("Digite o endereço: ")
        cpf_user = input("Digite o cpf: ")
        cadastrar_usuario(nome_user, endereco_user, cpf_user)

    elif escolha == 6:
        listar_usuarios()

    #7. Sair
    elif escolha == 7:
        print("\nObrigado por usar a biblioteca. Até logo!")
        break #Quebra o loop

    #Erro
    else:
        print("\nOpção inválida. Por favor, escolha um número de 1 a 7.")