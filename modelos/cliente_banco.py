class ClienteBanco:
    def __init__(self, nome, idade, sexo, cpf, telefone):
        self.nome = nome
        self.idade = idade
        self.sexo = sexo
        self.cpf = cpf
        self.telefone = telefone

    @classmethod
    def alterar_idade(cls, cliente, nova_idade):
        cliente.idade = nova_idade

    def alterar_idade(self, nova_idade):
        self.idade = nova_idade

cliente1 = ClienteBanco('Bruno','21','Masculino','123.456.789-10','123-4567-8901')
cliente2 = ClienteBanco('Tialy','20','Feminino','123.456.789-11','123-4567-8902')
cliente3 = ClienteBanco('Funalo','22','Masculino','123.456.789-12','123-4567-8903')

print (cliente1.idade)
ClienteBanco.alterar_idade(cliente1, 22)
print (cliente1.idade)
cliente1.alterar_idade(23)
print(cliente1.idade)