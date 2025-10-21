#Otimizando sistema bancário utilizando funções, desafo proposto no bootcamp da DIO.

#Importando biblioteca que será usada
import textwrap

#Função refatorada do código para exibir menu
def exibir_menu():
    """Exibe o menu de opções para o usuário."""
    menu = """
    ================ MENU ================
    [d]  Depositar
    [s]  Sacar
    [e]  Extrato
    [nu] Novo Usuário
    [nc] Nova Conta
    [lc] Listar Contas
    [q]  Sair
    => """
    #textwrap.dedent remove a indentação inicial da string
    return textwrap.dedent(menu)

#Função refatorada para depósito em conta
def depositar(contas):
    """Realiza um depósito em uma conta específica."""
    try:
        numero_conta = int(input("Informe o número da conta: "))
        conta = buscar_conta(numero_conta, contas)

        if not conta:
            print("Operação falhou! Conta não encontrada.")
            return

        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            conta["saldo"] += valor
            conta["extrato"] += f"Depósito:\t\tR$ {valor:.2f}\n"
            print("=== Depósito realizado com sucesso! ===")
        else:
            print("Operação falhou! O valor informado é inválido.")
            
    except ValueError:
        print("Operação falhou! Valor de entrada inválido (use apenas números).")

#Função refatorada para saque de conta
def sacar(contas, limite_valor, limite_saques):
    """Realiza um saque de uma conta específica, validando os limites."""
    try:
        numero_conta = int(input("Informe o número da conta: "))
        conta = buscar_conta(numero_conta, contas)

        if not conta:
            print("Operação falhou! Conta não encontrada.")
            return

        valor = float(input("Informe o valor do saque: "))

        saldo = conta["saldo"]
        numero_saques = conta["numero_saques"]

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite_valor
        excedeu_saques = numero_saques >= limite_saques

        if excedeu_saldo:
            print("Operação falhou! Você não tem saldo suficiente.")
        elif excedeu_limite:
            print("Operação falhou! O valor do saque excede o limite (R$ 500.00).")
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques (3) excedido.")
        elif valor > 0:
            conta["saldo"] -= valor
            conta["extrato"] += f"Saque:\t\t\tR$ {valor:.2f}\n"
            conta["numero_saques"] += 1
            print("=== Saque realizado com sucesso! ===")
        else:
            print("Operação falhou! O valor informado é inválido.")

    except ValueError:
        print("Operação falhou! Valor de entrada inválido (use apenas números).")

#Função refatorada para exibir extrato da conta
def exibir_extrato(contas):
    """Exibe o extrato de transações e o saldo de uma conta específica."""
    try:
        numero_conta = int(input("Informe o número da conta: "))
        conta = buscar_conta(numero_conta, contas)

        if not conta:
            print("Operação falhou! Conta não encontrada.")
            return

        print("\n================ EXTRATO ================")
        extrato = conta["extrato"]
        saldo = conta["saldo"]
        
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo:\t\t\tR$ {saldo:.2f}")
        print("==========================================")

    except ValueError:
        print("Operação falhou! Número da conta inválido.")

#Função nova implementada, cadastro de usuário(cliente)
def cadastrar_usuario(usuarios):
    """Cadastra um novo usuário (cliente) no sistema."""
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("Operação falhou! Já existe usuário com esse CPF.")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (DD-MM-AAAA): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    #Armazena o usuário como um dicionário na lista de usuários
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })

    print("=== Usuário cadastrado com sucesso! ===")

#Função nova implementada, cadastro de conta bancária
def cadastrar_conta_bancaria(agencia, usuarios, contas):
    """Cria uma nova conta bancária vinculada a um usuário existente."""
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Operação falhou! Usuário não encontrado. Cadastre o usuário primeiro.")
        return

    #O número da conta será sequencial (1, 2, 3...)
    numero_conta = len(contas) + 1
    
    #Cria um dicionário para a conta
    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta,
        "usuario": usuario,
        "saldo": 0,
        "extrato": "",
        "numero_saques": 0
    }
    
    contas.append(conta)

    print(f"=== Conta {numero_conta} cadastrada com sucesso para o usuário {usuario['nome']}! ===")

#Função nova implementada, exibição das contas em listas
def listar_contas(contas):
    """Exibe uma lista de todas as contas cadastradas."""
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
        
    print("================ LISTA DE CONTAS ================")
    for conta in contas:
        linha = f"""
        Agência:\t{conta['agencia']}
        C/C:\t\t{conta['numero_conta']}
        Titular:\t{conta['usuario']['nome']}
        """
        print(textwrap.dedent(linha))
    print("=================================================")


#---Funções Auxiliares---

#Implementando funções auxiliares para reduzir reétição de código
def filtrar_usuario(cpf, usuarios):
    """Busca um usuário na lista de usuários pelo CPF."""
    #List comprehension: cria uma lista de usuários onde o CPF bate
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    #Retorna o primeiro usuário encontrado ou None se a lista estiver vazia
    return usuarios_filtrados[0] if usuarios_filtrados else None

def buscar_conta(numero_conta, contas):
    """Busca uma conta na lista de contas pelo número."""
    contas_filtradas = [conta for conta in contas if conta["numero_conta"] == numero_conta]
    return contas_filtradas[0] if contas_filtradas else None


#---Função Principal---

def main():
    """Função principal que executa o sistema bancário."""
    #Constantes do banco
    LIMITE_VALOR_SAQUE = 500
    LIMITE_SAQUES_DIARIOS = 3
    AGENCIA = "0001"

    #Estruturas de dados para armazenar o estado do sistema
    usuarios = []
    contas = []

    while True:
        opcao = input(exibir_menu()).strip().lower() #Pega a opção e formata

        if opcao == 'd':
            depositar(contas)
        
        elif opcao == 's':
            sacar(contas, LIMITE_VALOR_SAQUE, LIMITE_SAQUES_DIARIOS)

        elif opcao == 'e':
            exibir_extrato(contas)
        
        elif opcao == 'nu':
            cadastrar_usuario(usuarios)

        elif opcao == 'nc':
            cadastrar_conta_bancaria(AGENCIA, usuarios, contas)
        
        elif opcao == 'lc':
            listar_contas(contas)

        elif opcao == 'q':
            print("Obrigado por usar nosso sistema. Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


#Garante que a função main() só será executada quando o script for rodado diretamente
if __name__ == "__main__":
    main()