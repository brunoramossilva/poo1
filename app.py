from modelos.animal import Animal

toby = Animal('Toby', 'Vira-lata')
mel = Animal('Mel', 'Gata')

toby.definir_responsavel('Bruno', '12345')
toby.definir_responsavel('Edna', '67890')

mel.definir_responsavel('Felipe', '24680')


def main():
    Animal.listar_animais()

toby.alternar_status_vacinacao()

if __name__ == '__main__':
    main()
