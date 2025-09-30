# user = input("Digite o nome de usuário: ")
# senha = int(input("Digite a senha: "))

# if user == 'admin' and senha == 1234:
#     print("Acesso Permitido!")
# else:
#     print("Acesso Negado")

#--------------------------------------------------

# n1 = float(input("Digite um número: "))
# n2 = float(input("Digite outro número: "))
# operador = input("Escolha o operador(+, -, *, /, %, **, //): ")

# if operador == "+":
#     resultado = n1 + n2
# elif operador == "-":
#     resultado = n1 - n2
# elif operador == "*":
#     resultado = n1 * n2
# elif operador == "/":
#     if n2 != 0:
#         resultado = n1 / n2
#     else:
#         resultado = "Divisão por zero!"
# elif operador == "%":
#     resultado = n1 % n2
# elif operador == "**":
#     resultado = n1 ** n2
# elif operador == "//":
#     if n2 != 0:
#         resultado = n1 // n2
#     else:
#         resultado = "Divisão por zero!"
# else:
#     resultado = "Operador Inválido!"

# print(resultado)

#------------------------------------------

metros = float(input("Digite o valor que deseja converter em metros: "))
medida = input("Digite a medida que deseja(cm, mm): ")

if medida == "cm":
    valor = metros * 100
elif medida == "mm":
    valor = metros * 1000
else:
    valor = "Medida indisponível"

print(valor)