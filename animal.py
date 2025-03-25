class Animal:
    def __init__(self, nome, raca):
        self.nome = nome
        self.raca = raca
        self.vacinacao = False

    def __str__(self):
            return f'O nome do animal é {self.nome}, da raça {self.raca}.'

toby = Animal('Toby', 'Vira-lata')

print(toby)
#