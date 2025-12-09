class Veiculo:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False #Atributo comum

    def ligar(self):
        self.ligado = True
        print("Veiculo ligado!")
        

    def desligar(self):
        self.ligado = False
        print("Veiculo desligado!")

    def exibir_dados(self):
        print(f"Veículo: {self.marca}, {self.modelo}, ({self.ano})")


###2. Classes Filhas (Subclasses): `Carro` e `Moto`

#Estas classes herdam tudo de `Veiculo` e adicionam suas próprias especializações.

class Carro(Veiculo): #Carro é um Veiculo
    def __init__(self, marca, modelo, ano, numero_portas):
        #1. Chama o construtor da classe pai (Veiculo) para inicializar marca, modelo e ano.
        super().__init__(marca, modelo, ano)
        #2. Inicializa o atributo específico da classe Carro.
        self.numero_portas = numero_portas

    #Sobrescrevendo o método exibir_dados para adicionar informação extra
    def exibir_dados(self):
        #1. Chama super().exibir_dados() para mostrar os dados básicos
        super().exibir_dados()
        #2. Depois, imprime o número de portas
        print(f"Portas: {self.numero_portas}")


class Moto(Veiculo): #Moto é um Veiculo
    def __init__(self, marca, modelo, ano, cilindradas):
        #1. Chama o construtor da classe pai (Veiculo).
        super().__init__(marca, modelo, ano)
        #2. Inicializa o atributo específico da classe Moto.
        self.cilindradas = cilindradas

    #Método específico da Moto
    def empinar(self):
       #Imprime uma mensagem divertida que só a moto pode fazer.
        print("Moto está empinando! randandandan")


# --- Área de Testes ---

#Criando objetos
meu_carro = Carro("Ford", "Ka", 2005, 2)
minha_moto = Moto("Honda", "Fan 160", 2025, 160)

print("\n--- Carro ---")
meu_carro.ligar()        #Método herdado
meu_carro.exibir_dados() #Método sobrescrito/especializado


print("\n--- Moto ---")
minha_moto.ligar()       #Método herdado
minha_moto.exibir_dados() #Método herdado (não sobrescrevemos na Moto, ela usa o do Veiculo)
minha_moto.empinar()     #Método específico