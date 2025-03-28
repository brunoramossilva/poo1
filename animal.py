class Animal:

    animais = []

    def __init__(self, nome, raca):
        self._nome = nome.title()
        self._raca = raca.title()
        self._vacinacao = False
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

def criando_animal():
    animal = [animal.strip() for animal in input('Digite o nome e a raça do '
    'animal separados por vírgula: ').split(',')]
    return Animal(*animal)

toby = Animal('Toby', 'Vira-lata')
mel = Animal('Mel', 'Gata')
Saddam = Animal('Saddam', 'Vira-lata')
Saddam._vacinacao = True
Pandinha = Animal('Pandinha', 'Chihuahua')
criando_animal()

Animal.listar_animais()
