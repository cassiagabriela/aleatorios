def show(m):
    print('Jogo da Velha')
    print(f'{m[0]}   {m[1]}   {m[2]} ')
    print(f'{m[3]}   {m[4]}   {m[5]} ')
    print(f'{m[6]}   {m[7]}   {m[8]} ')


def jogadaX(tabela, localX):

    while True:
        try:
            if int(localX) not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or str(localX).isalpha() or len(str(localX).strip())==0:
                localX = input('Posição invalida, tente novamente: ')
                continue
            else:
                posicao = int(localX) - 1
                if tabela[posicao] == 'X' or tabela[posicao] == 'O':
                    localX = input('Posição ocupada, tente novamente: ')
                    continue
                else:
                    tabela[posicao] = 'X'
                    return tabela
        except:
            localX = input('Não use letras. Esse menu aceita apenas números, tente novamente: ')



def jogadaO(tabela, localO):
    while True:
        try:
            if int(localO) not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or str(localO).isalpha() or len(str(localO).strip()) == 0:
                localO = input('Posição invalida, tente novamente: ')
                continue
            else:
                posicao = int(localO) - 1
                if tabela[posicao] == 'X' or tabela[posicao] == 'O':
                    localO = input('Posição ocupada, tente novamente: ')
                    continue
                else:
                    tabela[posicao] = 'O'
                    return tabela
        except:
            localO = input('Não use letras. Esse menu aceita apenas números, tente novamente: ')


def vitoria(m):
    if (m[0] == 'O' and m[1] == 'O' and m[2] == 'O') or (m[3] == 'O' and m[4] == 'O' and m[5] == 'O'):
        return True

    elif (m[6] == 'O' and m[7] == 'O' and m[8] == 'O') or (m[2] == 'O' and m[5] == 'O' and m[8] == 'O'):
        return True

    elif (m[0] == 'O' and m[3] == 'O' and m[6] == 'O') or (m[1] == 'O' and m[4] == 'O' and m[7] == 'O'):
        return True

    elif (m[0] == 'O' and m[4] == 'O' and m[8] == 'O') or (m[6] == 'O' and m[4] == 'O' and m[2] == 'O'):
        return True

    elif (m[0] == 'X' and m[1] == 'X' and m[2] == 'X') or (m[3] == 'X' and m[4] == 'X' and m[5] == 'X'):
        return True

    elif (m[6] == 'X' and m[7] == 'X' and m[8] == 'X') or (m[2] == 'X' and m[5] == 'X' and m[8] == 'X'):
        return True

    elif (m[0] == 'X' and m[3] == 'X' and m[6] == 'X') or (m[1] == 'X' and m[4] == 'X' and m[7] == 'X'):
        return True

    elif (m[0] == 'X' and m[4] == 'X' and m[8] == 'X') or (m[6] == 'X' and m[4] == 'X' and m[2] == 'X'):
        return True

    else:
        return False


def velha(tab):
    cont = 0
    for i in tab:
        if i=='X' or i=='O':
            cont += 1
            if cont == 9:
                print('Deu velhaa.. perderam')
                return True




if __name__ == '__main__':
    tabela = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    # matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    jogador1 = input('Qual o nome do primeiro jogador: ')
    jogador2 = input('Qual o nome do segundo jogador: ')

    while True:
        show(tabela)
        place = input(f'{jogador1} qual posição deseja colocar a sua peça (X)? ')
        tabela = jogadaX(tabela, place)

        if vitoria(tabela):
            show(tabela)
            print(f'Parabéns, {jogador1} venceu!!!')
            a = input('Deseja jogar novamente? sim ou nao? ')
            #simm
            while a != 'sim' and a != 'nao':
                a = input('vc digitou errado, tente novamente (sim ou nao): ')

            if a == 'sim':
                tabela = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                continue
            else:
                print("Belo jogo, até a próxima")
                break
        elif velha(tabela):
            show(tabela)
            a = input('Deseja jogar novamente? sim ou nao? ')
            while a != 'sim' and a != 'nao':
                a = input('vc digitou errado, tente novamente (sim ou nao): ')

            if a == 'sim':
                tabela = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                continue
            else:
                print("Belo jogo, até a próxima")
                break

        elif (not vitoria(tabela)) or (not velha(tabela)):
            show(tabela)
            place = input(f'{jogador2} qual posição deseja colocar a sua peça (O)? ')
            tabela = jogadaO(tabela, place)
            if vitoria(tabela):
                show(tabela)
                print(f'Parabéns, {jogador2} venceu!!!')

                a = input('Deseja jogar novamente? sim ou nao? ')
                while a != 'sim' and a != 'nao':
                    a = input('vc digitou errado, tente novamente (sim ou nao): ')

                if a == 'sim':
                    tabela = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    continue
                else:
                    print("Belo jogo, até a próxima")
                    break
            elif velha(tabela):
                show(tabela)
                a = input('Deseja jogar novamente? sim ou nao? ')

                while a != 'sim' and a != 'nao':
                    a = input('vc digitou errado, tente novamente (sim ou nao): ')

                if a == 'sim':
                    tabela = [1, 2, 3, 4, 5, 6, 7, 8, 9]
                    continue
                else:
                    print("Belo jogo, até a próxima")
                    break


