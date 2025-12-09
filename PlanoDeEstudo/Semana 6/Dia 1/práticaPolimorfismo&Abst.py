from abc import ABC, abstractmethod

#1. CLASSE ABSTRATA (O Contrato)
#Ela herda de ABC (Abstract Base Class)
class Funcionario(ABC):
    def __init__(self, nome):
        self.nome = nome

    #Este decorador @abstractmethod diz: "Classes filhas, vocês SÃO OBRIGADAS a criar este método"
    @abstractmethod
    def calcular_salario(self):
        pass



#2. CLASSES CONCRETAS (Quem faz o trabalho)

class FuncionarioCLT(Funcionario):
    def __init__(self, nome, salario_mensal):
        super().__init__(nome)
        self.salario_mensal = salario_mensal

    def calcular_salario(self):
        return self.salario_mensal


class FuncionarioHorista(Funcionario):
    def __init__(self, nome, valor_hora, horas_trabalhadas):
        super().__init__(nome)
        self.valor_hora = valor_hora
        self.horas_trabalhadas = horas_trabalhadas

    def calcular_salario(self):
        return self.valor_hora * self.horas_trabalhadas
        


#--- Área de Testes (Polimorfismo em Ação) ---

#Criando os funcionários
func1 = FuncionarioCLT("Ana", 5000)
func2 = FuncionarioHorista("Carlos", 50, 160) #50 reais/hora * 160 horas

#Lista de funcionários (misturando tipos diferentes!)
equipe = [func1, func2]

print("--- Folha de Pagamento ---")

#O POLIMORFISMO ACONTECE AQUI:
#tratamos todos como "funcionario", mas cada um calcula do seu jeito.
for f in equipe:
    print(f"O salário de {f.nome} é R$ {f.calcular_salario()}")