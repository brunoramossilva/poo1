class ContaBancaria:
    def __init__(self, titular, saldo):
        self._titular = titular
        self._saldo = float(saldo) + 1000.50  # Adicionando 1000,50 ao saldo inicial
        self._ativo = False

    def __str__(self):
        return f'O nome do titular da conta é {self._titular}, seu saldo' \
        f' é de R$ {self._saldo} e o status da conta é {self.ativo}.'

    def alterar_status(self):
        self._ativo = not self._ativo

    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = not conta._ativo

    @classmethod
    def criar_conta(cls, titular, saldo = '0', tipo = 'comum'):
        return cls(titular, saldo)
    
    @property
    def ativo(self):
        return 'ativa' if self._ativo else 'inativa'
    
    @property
    def saldo(self):
        return self._saldo
    
    @property
    def titular(self):
        return self._titular
    
    @saldo.setter
    def saldo(self, novo_saldo):
        if isinstance(novo_saldo, float) and novo_saldo >= 0:
            self._saldo = novo_saldo
        else:
            raise ValueError('O saldo deve ser um número e também deve ser maior do que 0.')
        
conta1 = ContaBancaria('Bruno', '12500.00')
conta2 = ContaBancaria('Tialy', '3500.00')
conta3 = ContaBancaria('Funalo', '0')
conta_padrao = ContaBancaria.criar_conta('João', '1000.00')
ContaBancaria.ativar_conta(conta_padrao)

#conta_padrao.saldo = 1.0

conta4 = ContaBancaria.criar_conta('Maria', '2000.00')
print(f'O titular da conta 04 se chama {conta4.titular}.\n')

print(conta1)
print(conta2)
print(conta3)
print(conta4)
print(conta_padrao)
