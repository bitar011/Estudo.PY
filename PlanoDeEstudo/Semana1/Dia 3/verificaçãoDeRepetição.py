# Programa que recebe uma lista de números e imprime apenas os números únicos, sem repetição

# Recebe os números
entrada = input("Digite uma lista de números: ")
# Recebe os números em stings e converte para inteiros e coloca em lista
lista = [int(num) for num in entrada.split()]

# Lista para guardar os números sem repetição
unicos = []
# Pecorre a lista e verifica se os números se repetem
for num in lista:
    if num not in unicos:
        unicos.append(num)

# Mostra o Resultado
print("Os únicos são:", unicos)