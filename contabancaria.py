class ContaBancaria:
    def __init__(self, titular, saldo):
        self.titular = titular
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'O nome do titular da conta é {self.titular}, seu saldo é de {self.saldo} e o status da conta é {self._ativo}.'

    def alterar_status(self):
        self._ativo = not self._ativo

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = not conta._ativo




conta1 = ContaBancaria('Bruno', '12.500')
conta2 = ContaBancaria('Tialy', '3.500')
conta3 = ContaBancaria('Funalo', '0')

ContaBancaria.ativar_conta(conta3)
conta2.alterar_status()

print(conta1)
print(conta2)
print(conta3)