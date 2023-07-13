menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[uc] Cadastrar Usuário
[cc] Criar Conta Corrente
[q] Sair

=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

# Lista para armazenar os usuários
usuarios = []

# Lista para armazenar as contas correntes
contas = []

# Função para realizar saque
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1

    return saldo, extrato

# Função para realizar depósito
def deposito(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo, extrato

# Função para exibir o extrato
def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Função para cadastrar usuário
def cadastrar_usuario():
    nome = input("Informe o nome do usuário: ")
    data_nascimento = input("Informe a data de nascimento do usuário: ")
    cpf = input("Informe o CPF do usuário: ")
    endereco = input("Informe o endereço do usuário: ")

    # Verifica se o CPF já está cadastrado
    cpf_existente = any(usuario["cpf"] == cpf for usuario in usuarios)

    if cpf_existente:
        print("Operação falhou! Já existe um usuário cadastrado com o CPF informado.")
    else:
        usuarios.append({
            "nome": nome,
            "data_nascimento": data_nascimento,
            "cpf": cpf,
            "endereco": endereco
        })
        print("Usuário cadastrado com sucesso!")

# Função para criar conta corrente
def criar_conta_corrente():
    cpf = input("Informe o CPF do usuário para associar a conta corrente: ")

    # Filtra a lista de usuários buscando o CPF informado
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)

    if usuario is None:
        print("Operação falhou! Não foi encontrado um usuário com o CPF informado.")
    else:
        numero_conta = len(contas) + 1
        contas.append({
            "agencia": "0001",
            "numero_conta": numero_conta,
            "usuario": usuario
        })
        print("Conta corrente criada com sucesso!")

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = deposito(saldo, valor, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato = saque(saldo=saldo, valor=valor, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

    elif opcao == "e":
        exibir_extrato(saldo, extrato=extrato)

    elif opcao == "uc":
        cadastrar_usuario()

    elif opcao == "cc":
        criar_conta_corrente()

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
