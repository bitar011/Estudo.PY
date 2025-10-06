nota = float(input("Digite sua nota: "))

if nota < 5:
    print("Reprovado")
elif nota < 7 and nota >= 5:
    print("Recuperação")
else:
    print("Aprovado!")