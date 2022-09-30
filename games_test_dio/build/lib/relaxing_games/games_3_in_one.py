from random import randint


def par_ou_impar():
    list_escolha = ['par', 'impar']
    num_pc = randint(1, 10)
    num_escolha_pc = randint(0, 1)
    escolha_pc = list_escolha[num_escolha_pc]
    num_usuario = int(input('Escolha um número de 1 a 10: '))
    escolha_usuario = str(input('Escolha entre par ou impar: ')).lower()
    total = num_pc + num_usuario
    resultado = ''
    if len(escolha_pc) == len(escolha_usuario):
        resultado = 'O jogo deu EMPATE !!!'
    else:
        if total % 2 == 0 and escolha_pc == 'par' or total % 2 == 1 and escolha_pc == 'impar':
            resultado = 'O computador GANHOU !!!'
        elif total % 2 == 0 and escolha_usuario == 'par' or total % 2 == 1 and escolha_usuario == 'impar':
            resultado = 'O usuário GANHOU !!!'
    print(f'Número escolhido pelo computador foi {num_pc}'
          f'\nFoi escolhido pelo computador um número {escolha_pc}'
          f'\nNúmero escolhido pelo usuário foi {num_usuario}'
          f'\nFoi escolhido pelo usuário um número {escolha_usuario}'
          f'\nA soma dos números foi em um total de {total}'
          f'\n{resultado}')


def pedra_papel_tesoura():
    list_item = ['pedra', 'papel', 'tesoura']
    num_pc = randint(0, 2)
    obj_pc = list_item[num_pc]
    obj_usuario = str(input('Escolha entre papel, pedra e tesoura: ')).lower()
    if obj_pc == 'pedra' and obj_usuario == 'tesoura' or obj_pc == 'papel' and obj_usuario == 'pedra' \
            or obj_pc == 'tesoura' and obj_usuario == 'papel':
        resultado = 'O computador GANHOU!!!'
    elif obj_usuario == 'pedra' and obj_pc == 'tesoura' or obj_usuario == 'papel' and obj_pc == 'pedra' \
            or obj_usuario == 'tesoura' and obj_pc == 'papel':
        resultado = 'O usuário GANHOU!!!'
    else:
        resultado = 'O jogo deu EMPATE!!!'
    print(f'O computador escolheu {obj_pc}'
          f'\nO usuário escolheu {obj_usuario}'
          f'\n{resultado}')


def jogo21():
    cartas_pc = []
    cartas_usuario = []
    cartas_mesa = []
    total = 0
    for n in range(6):
        inicial = randint(1, 10)
        if n < 3:
            cartas_pc.append(inicial)
        else:
            cartas_usuario.append(inicial)
    print(f'PC {cartas_pc}'
          f'\nUsuário {cartas_usuario}'
          f'\nMesa {cartas_mesa}')
    while total < 21:
        print('\nVez do usuario \n')
        descarte = int(input(f'Escolha a carta que deseja descartar ou 0 para pular: \n{cartas_usuario}\nR:'))
        if descarte in cartas_usuario:
            total = total + descarte
            print(f'Total da mesa = {total}')
            cartas_usuario.remove(descarte)
            cartas_usuario.append(randint(1, 10))
        elif descarte == 0:
            print(f'Total da mesa = {total}. Nao houve descarte nesta rodada')
            cartas_usuario.append(randint(1, 10))
        if total == 21:
            print('Parabéns, você VENCEU!!!')
            break
        elif total > 21:
            print('Jogada errada. Você PERDEU!!!')
            break
        print('\nVez do computador \n')
        descarte = 0
        for carta in cartas_pc:
            if total + carta <= 21 and carta > descarte:
                descarte = carta
        if descarte in cartas_pc:
            total = total + descarte
            print(f'Computador jogou {descarte}')
            print(f'Total da mesa = {total}')
            cartas_pc.remove(descarte)
            cartas_pc.append(randint(1, 10))
        elif descarte == 0:
            print(f'Total da mesa = {total}. Nao houve descarte nesta rodada')
            cartas_pc.append(randint(1, 10))
        if total == 21:
            print('O PC venceu, voce perdeu!!')
            break
        elif total > 21:
            print('Pc jogou errado. Voce venceu!')
            break


def escolher_game():
    game = int(input('Digite o número do jogo desejado: \n1. Pedra, papel e tesoura \n2. 21 \n3.Par ou impar '
                     '\nNúmero: '))
    return game


def iniciar_game(continuar_game='s'):
    game = escolher_game()
    while continuar_game == 's':
        if game == 1:
            pedra_papel_tesoura()
        elif game == 2:
            jogo21()
        elif game == 3:
            par_ou_impar()
        else:
            print('Jogo desconhecido. Escolher novamente!')
        continuar_game = input('Deseja continuar jogando ? \nSim / Não \nR: ').lower()[0]
        if continuar_game == 's':
            game = escolher_game()
        else:
            print('Jogo Encerado !!!')


iniciar_game()
