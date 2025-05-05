from modelos.responsaveis import Responsavel

class Animal:

    animais = []

    def __init__(self, nome, raca):
        self._nome = nome.title()
        self._raca = raca.title()
        self._vacinacao = False
        self._responsavel = []
        Animal.animais.append(self)

    @classmethod
    def listar_animais(cls):
        print('-' * 85)
        print(f'| {'# Nome do Animal #'.ljust(25)} | {'# Raça do Animal #'.ljust(25)} | {'# Status de Vacinação #'.ljust(25)} |')
        print('-' * 85)
        for animal in cls.animais:
            print(f'| {animal._nome.ljust(25)} | {animal._raca.ljust(25)} | {animal.vacinacao.ljust(25)} |')
            print('-' * 85)

    @property
    def vacinacao(self):
        return 'Vacinado(a)' if self._vacinacao else 'Não Vacinado(a)'
    
    def alternar_status_vacinacao(self):
        self._vacinacao = not self._vacinacao


    def definir_responsavel(self, nome, idade):
        responsavel = Responsavel(nome, idade)
        self._responsavel.append(responsavel)

    def media_idades(self):
        if not self._responsavel:
            return 0
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
