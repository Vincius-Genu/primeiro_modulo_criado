def jogo_completo():
    game = []
    for a in range(9):
        game.append(list(map(int, input().split())))
    return game


def check_linha(lista):
    for linha in range(9):
        if len(set(lista[linha])) != len(lista[linha]):
            return False
    return True


def check_coluna(lista):
    matriz_coluna = []
    for coluna in range(9):
        vetor_coluna = []
        for linha in range(9):
            vetor_coluna.append(lista[linha][coluna])
        matriz_coluna.append(vetor_coluna)
        if len(set(matriz_coluna[coluna])) != len(matriz_coluna[coluna]):
            return False
    return True


def check_regiao(lista):
    inicio1 = inicio2 = 0
    fim1 = fim2 = 3
    count1 = count2 = 0
    matriz_regiao = []
    for regiao in range(9):
        vetor_regiao = []
        count1 += 1
        if count1 in [4]:
            inicio1 = 3
            fim1 = 6
        elif count1 in [7]:
            inicio1 = 6
            fim1 = 9
        for linha in range(inicio1, fim1):
            count2 += 1
            if count2 in [4, 13, 22]:
                inicio2 = 3
                fim2 = 6
            elif count2 in [7, 16, 25]:
                inicio2 = 6
                fim2 = 9
            elif count2 in [10, 19]:
                inicio2 = 0
                fim2 = 3
            for coluna in range(inicio2, fim2):
                vetor_regiao.append(lista[linha][coluna])
        matriz_regiao.append(vetor_regiao)
        if len(set(matriz_regiao[regiao])) != len(matriz_regiao[regiao]):
            return False
    return True


teste = int(input())
passou = True
for n in range(teste):
    matriz_jogo = jogo_completo()
    checagem_linha = check_linha(matriz_jogo)
    checagem_coluna = check_coluna(matriz_jogo)
    checagem_regiao = check_regiao(matriz_jogo)
    if checagem_linha == passou and checagem_coluna == passou and checagem_regiao == passou:
        print(f'Instancia {n + 1}'
              f'\nSIM\n')
    else:
        print(f'Instancia {n + 1}'
              f'\nNAO\n')
