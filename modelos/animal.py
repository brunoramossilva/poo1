from modelos.responsaveis import Responsavel

class Animal:

    animais = []

    def __init__(self, nome, raca):
        self._nome = nome.title()
        self._raca = raca.title()
        self._vacinacao = False
        self._responsavel = []
        Animal.animais.append(self)

    def definir_responsavel(self, nome, idade):
        responsavel = Responsavel(nome, idade)
        self._responsavel.append(responsavel)

    @classmethod
    def listar_animais(cls):
        tam_linha = 153
        print('-' * tam_linha)
        print(f'| {'# Nome do Animal #'.ljust(25)} | {'# Raça do Animal #'.ljust(25)} | {'# Status de Vacinação #'.ljust(25)} | {'# Responsáveis #'.ljust(25)} | {'# Média das Idades dos Responsáveis #'.ljust(25)} |')
        print('-' * tam_linha)
        for animal in cls.animais:
            print(f'| {animal._nome.ljust(25)} | {animal._raca.ljust(25)} | {animal.vacinacao.ljust(25)} | {animal.responsaveis.ljust(25)} | {str(animal.media_idades).ljust(37)} |')
            print('-' * tam_linha)

    @property
    def vacinacao(self):
        return 'Vacinado(a)' if self._vacinacao else 'Não Vacinado(a)'
    
    def alternar_status_vacinacao(self):
        self._vacinacao = not self._vacinacao

    @property
    def responsaveis(self):
        if not self._responsavel:
            return "Não há responsáveis"
        responsaveis = [responsavel._nome for responsavel in self._responsavel]
        return ", ".join(responsaveis)

    @property
    def media_idades(self):
        if not self._responsavel:
            return "N/A"
        soma_das_idades = sum(responsavel._idade for responsavel in self._responsavel)
        quantidade_das_idades = len(self._responsavel)
        media = round(soma_das_idades / quantidade_das_idades, 1)
        return media

def criando_animal():
    pergunta = input('Deseja criar um novo animal? (Y/N): ')
    if pergunta.lower() == 'y':
        animal = (animal.strip() for animal in input('Digite o nome e a raça do animal ' \
        'separados por uma vírgula: ').split(','))
        return Animal(*animal)


""" toby = Animal('Toby', 'Vira-lata')
mel = Animal('Mel', 'Gata')
Saddam = Animal('Saddam', 'Vira-lata')
Saddam.alternar_status_vacinacao()
Pandinha = Animal('Pandinha', 'Chihuahua')
criando_animal()

Animal.listar_animais() """
