#Calculando com i/o, variáveis e condições
n1 = float(input("Digite um número: "))
n2 = float(input("Digite outro número: "))
operador = input("Escolha o operador(+, -, *, /, %, **, //): ")

if operador == "+":
    resultado = n1 + n2
elif operador == "-":
    resultado = n1 - n2
elif operador == "*":
    resultado = n1 * n2
elif operador == "/":
    if n2 != 0:
        resultado = n1 / n2
    else:
        resultado = "Divisão por zero!"
elif operador == "%":
    resultado = n1 % n2
elif operador == "**":
    resultado = n1 ** n2
elif operador == "//":
    if n2 != 0:
        resultado = n1 // n2
    else:
        resultado = "Divisão por zero!"
else:
    resultado = "Operador Inválido!"

print(resultado)
