class ContaBancaria:
    taxaDeRendimento = 0.05
    
    def __init__(self, titular, saldo = 0.0):
        self.titular = titular
        self.saldo = saldo
        

    def depositar(self, valor):
        self.saldo += valor
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!\n")

    def sacar(self, valor):
        if self.saldo >= valor:
            self.saldo -= valor
            print(f"Saque de R$ {valor:.2f} realizado com sucesso!\n")
        else:
            print(f"Saldo insuficiente! Seu saldo atual é de R$ {self.saldo:.2f}")

    @classmethod
    def mudar_taxa(cls, nova_taxa):
        cls.taxaDeRendimento = nova_taxa
        print(f"Nova taxa de rendimento do banco: {nova_taxa * 100}%\n")

class ContaPoupanca(ContaBancaria):

    def rendimento(self):
        ganho = self.saldo * self.taxaDeRendimento
        self.saldo += ganho
        print(f"Rendimento de R$ {ganho:.2f} aplicado!")

"""
minhaConta = ContaBancaria("Lucas", 580.00)

print(f"Titular: {minhaConta.titular} | Saldo inicial: R$ {minhaConta.saldo:.2f}\n")

minhaConta.depositar(420.00)
print(f"Saldo após o depósito: R$ {minhaConta.saldo:.2f}\n")

minhaConta.sacar(200.00)
print(f"Saldo após o saque: R$ {minhaConta.saldo:.2f}")
"""

poupanca = ContaPoupanca("Lopes", 1000.00)

poupanca.rendimento()
print(f"Saldo atual: R$ {poupanca.saldo:.2f}")

ContaBancaria.mudar_taxa(0.10)

poupanca.rendimento()
print(f"Saldo final: R$ {poupanca.saldo:.2f}\n  ")

