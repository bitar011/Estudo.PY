#Prática de funções
#Função que calcula área

#Função com calculo a ser feito
def calcular_area(largura, altura):
    area = largura * altura
    return area

#Pede e recebe os valores ao usuário
largura_user = float(input("Digite a largura em metros(m): "))
altura_user = float(input("Digite a altura em metros(m): "))

#Chama a função e utiliza os valores inseridos pelo usuário
print(calcular_area(largura_user, altura_user))