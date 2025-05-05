from modelos.animal import Animal

toby = Animal('Toby', 'Vira-lata')
mel = Animal('Mel', 'Gata')
pipoca = Animal('Pipoca','Cadela')

def main():
    Animal.listar_animais()

toby.alternar_status_vacinacao()

if __name__ == '__main__':
    main()
