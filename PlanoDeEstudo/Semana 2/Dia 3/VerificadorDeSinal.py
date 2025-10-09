#Verificador de sinal, utilizando condicionais

#Função que verifica o sinal recebido usando as condições para definir e retornar sua natureza
def verificar_sinal(n):
    if n > 0:
       return "Positivo!"
    elif n < 0:
        return "Negativo!"
    else:
        return "Zero!"

#Recebe o sinal do usuário
numero_do_usuario = int(input("Digite um número como sinal: "))

#Chama a função para verificar a natureza do sinal recebida
print(verificar_sinal(numero_do_usuario))