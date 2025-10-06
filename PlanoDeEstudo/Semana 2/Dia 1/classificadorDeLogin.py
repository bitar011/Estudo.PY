#Veerificador de login

#Recebe usuário e senha
user = input("Digite o nome de usuário: ")
senha = input("Digite a senha: ")

#Verifica usuário e senha, e retorna a categoria de cada um
if user == "admin" and senha == "1234":
    print("Login de administrador bem-sucedido!")
elif user == "convidado" and senha == "guest":
    print("Login de convidado autorizado.")
else:
    print("Usuário ou senha inválidos.")