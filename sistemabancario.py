class Banco:
    def __init__(self):
        self.saldo = 0
        self.depositos = []
        self.saques = []

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.depositos.append(valor)
            print(f"Depósito de R$ {valor:.2f} realizado com sucesso.")
        else:
            print("O valor do depósito deve ser positivo.")

    def sacar(self, valor):
        if valor > 0:
            if valor <= 500 and len(self.saques) < 3 and self.saldo >= valor:
                self.saldo -= valor
                self.saques.append(valor)
                print(f"Saque de R$ {valor:.2f} realizado com sucesso.")
            elif len(self.saques) >= 3:
                print("Limite diário de saques atingido.")
            elif self.saldo < valor:
                print("Saldo insuficiente.")
            else:
                print("Valor inválido para saque.")
        else:
            print("O valor do saque deve ser positivo.")

    def extrato(self):
        print("Extrato:")
        if len(self.depositos) == 0 and len(self.saques) == 0:
            print("Não foram realizadas movimentações.")
        else:
            for deposito in self.depositos:
                print(f"Depósito: R$ {deposito:.2f}")
            for saque in self.saques:
                print(f"Saque: R$ {saque:.2f}")
        print(f"Saldo atual: R$ {self.saldo:.2f}")


# Função para exibir o menu e receber a opção do usuário
def exibir_menu():
    print("Digite 1 para saldo")
    print("Digite 2 para deposito")
    print("Digite 3 para extrato")
    print("Digite 4 para saque")
    print("Digite 0 para sair")
    return int(input("Opcao: "))


# Exemplo de uso com menu interativo
banco = Banco()
opcao = exibir_menu()

while opcao != 0:
    if opcao == 1:
        print(f"Saldo atual: R$ {banco.saldo:.2f}")
    elif opcao == 2:
        valor = float(input("Digite o valor do depósito: "))
        banco.depositar(valor)
    elif opcao == 3:
        banco.extrato()
    elif opcao == 4:
        valor = float(input("Digite o valor do saque: "))
        banco.sacar(valor)
    
    print()  # Espaçamento para melhorar a visualização
    opcao = exibir_menu()

print("Sistema encerrado.")
