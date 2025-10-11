#Projeto semanal
#Refazendo primeiro projeto utilizando funções

#Função para ler anotações feitas
def ler_anotacoes():
    try:
        with open("notas.txt", "r") as f:
            print("\n--- Suas Anotações ---")
            print(f.read())
    except FileNotFoundError: #Falha caso não tenha nada para ler
        print("⚠ Ainda não há anotações.")

#Função para escrever, criar e adicionar ao bloco de notas
def escrever_anotacao(texto):
    with open("notas.txt", "a") as f:
        f.write(texto + "\n")
    print("Anotação salva!")

#Função que executa o bloco de notas com interativiadde
def executar():
    while True:
        print("\n=== Mini Bloco de Notas ===")
        print("1 - Escrever anotação")
        print("2 - Ler anotações")
        print("3 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            texto_user = input("Digite sua anotação: ")
            escrever_anotacao(texto_user)

        elif opcao == "2":
            ler_anotacoes()

        elif opcao == "3":
            print("Saindo... até logo!")
            break

        else:
            print("Opção inválida. Tente novamente.")

executar()