class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = float(saldo) + 1000.50  # Adicionando 1000 ao saldo inicial
        self._ativo = False

    def __str__(self):
        return f'O nome do titular da conta é {self.titular}, seu saldo é de {self.saldo} e o status da conta é {self._ativo}.'

    def alterar_status(self):
        self._ativo = not self._ativo

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = not conta._ativo

    @classmethod
    def criar_conta(cls, titular, saldo = '0', tipo = 'comum'):
        return cls(titular, saldo)

conta1 = ContaBancaria('Bruno', '12500.00')
conta2 = ContaBancaria('Tialy', '3500.00')
conta3 = ContaBancaria('Funalo', '0')
conta_padrao = ContaBancaria.criar_conta('João', '1000.00')

#ContaBancaria.ativar_conta()

print(conta1)
print(conta2)
print(conta3)
print(conta_padrao)