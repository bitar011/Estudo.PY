#Testando condiçoes com senha
user = input("Digite o nome de usuário: ")
senha = int(input("Digite a senha: "))

if user == 'admin' and senha == 1234:
    print("Acesso Permitido!")
else:
    print("Acesso Negado")