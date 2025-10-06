#Programa para calcular salário com base em horas, valor de hor, bônus de cargo e imposto

#Recebe informações do funcionário
nome = input("Digite seu nome: ")
cargo = input("Digite seu cargo: ")
horas = float(input("Digite suas horas trabalhadas: "))
valor = float(input("Digite o valor de suas horas: "))

#Calcula o salário bruto do funcionário
salario = horas * valor

#Calcula bônus do salário bruto
if cargo == "junior":
    salario_bonus = salario * 1.05 #Porcentagem de acrescímo por cargo -> 5%/10%/20%
elif cargo == "pleno":
    salario_bonus = salario * 1.1
else:
    salario_bonus = salario * 1.2
    
#Calcula desconto de imposto 
if salario_bonus < 2000:
    imposto = salario_bonus * 0.05
elif salario_bonus <= 5000:
    imposto = salario_bonus * 0.1
else:
    imposto = salario_bonus * 0.15

#Calcula o salário liquído com base nos bônus e descontos
salario_liquido = salario_bonus - imposto

#Retorna todas as informações
print(f"\nFuncionário: {nome}")
print(f"Cargo: {cargo.capitalize()}")
print(f"Salário bruto: R${horas * valor:.2f}")
print(f"Bônus aplicado: R${salario_bonus - (horas * valor):.2f}")
print(f"Imposto descontado: R${imposto:.2f}")
print(f"Salário líquido: R${salario_liquido:.2f}")
