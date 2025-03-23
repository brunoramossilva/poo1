class Animal:
    nome = ''
    raca = ''
    vacinacao = False

toby = Animal()
toby.nome = 'Toby'
toby.raca = 'Vira-lata'

mel = Animal()
mel.nome = 'Mel'
mel.raca = 'Gata'

print(vars(toby))
print(f'O nome do cachorro é {toby.nome} e ele é da raça {toby.raca}')