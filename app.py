from modelos.animal import Animal

toby = Animal('Toby', 'Vira-lata')
mel = Animal('Mel', 'Gata')

toby.definir_responsavel('Bruno', '21')
toby.definir_responsavel('Edna', '57')

mel.definir_responsavel('Felipe', '28')


def main():
    Animal.listar_animais()

toby.alternar_status_vacinacao()

if __name__ == '__main__':
    main()
