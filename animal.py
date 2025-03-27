class Animal:

    animais = []

    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
        self._vacinacao = False
        Animal.animais.append(self)

    def listar_animais():
        print('-' * 85)
        print(f'| {'# Nome do Animal #'.ljust(25)} | {'# Raça do Animal #'.ljust(25)} | {'# Status de Vacinação #'.ljust(25)} |')
        print('-' * 85)
        for animal in Animal.animais:
            print(f'| {animal.nome.ljust(25)} | {animal.raca.ljust(25)} | {animal.vacinacao.ljust(25)} |')
            print('-' * 85)

    @property
    def vacinacao(self):
        return 'Vacinado(a)' if self._vacinacao else 'Não Vacinado(a)'




toby = Animal('Toby', 'Vira-lata')
mel = Animal('Mel', 'Gata')
Saddam = Animal('Saddam', 'Vira-lata')
Pandinha = Animal('Pandinha', 'Chihuahua')

Animal.listar_animais()
