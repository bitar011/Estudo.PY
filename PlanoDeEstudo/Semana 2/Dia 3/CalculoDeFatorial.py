#Fatorando número com função e loops

#Função com calculo a ser feito
def calcular_fatorial(n):
    fatorial = 1 #Sempre começar em 1
    for n in range(1, n+1): #Loop q volta ao número para continuar guardando seu valor e seguir com a operação
        fatorial = fatorial * n
    return fatorial

#Recebe número do usuário
n_user = int(input("Digite o número inteiro que deseja fatorar: "))

#Chama a função e utiliza o número inserido pelo usuário
print(calcular_fatorial(n_user))