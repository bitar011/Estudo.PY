#Projeto da Semana

#Bloco de notas
while True:
    print("\n=== Mini Bloco de Notas ===")
    print("1 - Escrever anotação")
    print("2 - Ler anotações")
    print("3 - Sair")

    opcao = input("Escolha: ")

    if opcao == "1":
        texto = input("Digite sua anotação: ")
        with open("notas.txt", "a") as f:
            f.write(texto + "\n")
        print("✔ Anotação salva!")

    elif opcao == "2":
        try:
            with open("notas.txt", "r") as f:
                print("\n--- Suas Anotações ---")
                print(f.read())
        except FileNotFoundError:
            print("⚠ Ainda não há anotações.")

    elif opcao == "3":
        print("Saindo... até logo!")
        break

    else:
        print("Opção inválida. Tente novamente.")
