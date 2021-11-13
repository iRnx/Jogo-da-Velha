from random import randint
from time import sleep

pts_jogador = 0
pts_maquina = 0
velha = 0
while True:
    jogador = ''
    primeiro = ''
    vencedor = ''
    p1, p2, p3, p4, p5, p6, p7, p8, p9 = ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '
    lv = 'livre'
    pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9 = lv, lv, lv, lv, lv, lv, lv, lv, lv
    jogada = 0
    jogada_maquina = 0
    turnos = 1
    tabuleiro_inicial = '''
    --- COMO JOGAR ---
    Quando for sua vez, digite o número correspondente à posição no tabuleiro para fazer sua jogada nela.
    Por exemplo, digamos que você queira jogar no centro, então você digita 5.
         |     |     
      1  |  2  |  3  
    _____|_____|_____
         |     |     
      4  |  5  |  6  
    _____|_____|_____
         |     |     
      7  |  8  |  9  
         |     |     
        '''
    print(tabuleiro_inicial)
    print('Você quer ser X ou O ?', end='')
    while jogador != 'X' and jogador != 'O':
        jogador = str(input('Digite X ou O pressione ENTER para escolher: ')).strip().upper()
        if jogador != 'X' and jogador != 'O':
            print('Entrada Inválida')
    if jogador == 'X':
        maquina = 'O'
        print('Maquina é: O')
    elif jogador == 'O':
        maquina = 'X'
        print('Maquina é: X')

    while primeiro != 'EU' and primeiro != 'PC':
        primeiro = str(input('Digite EU para o Humano começar, ou digite PC para Maquina começar: ')).strip().upper()
        if primeiro != 'EU' and primeiro != 'PC':
            print('Entrada Inválida')
    if primeiro == 'EU':
        print('Humano joga primeiro!!')
    elif primeiro == 'PC':
        print('Maquina joga primeiro!!')


    def atualizar_tabuleiro():
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        tabuleiro = f'''
        |      |   
    {p1}   |  {p2}   |  {p3}
    ____|______|_____
        |      |
    {p4}   |  {p5}   |  {p6}
    ____|______|_____
        |      |
    {p7}   |  {p8}   |  {p9}
        |      |
        '''
        print(tabuleiro)


    def jogada_jogador1():
        global jogada
        while True:
            try:
                jogada = int(input('Digite a posição da sua jogada: '))
                break
            except ValueError:
                print('Valor digitado inválido, Digite um número inteiro válido de 1 a 9!')


    def verifica_jogador_ocupado():
        global jogada
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        jogada_jogador1()
        while jogada not in range(1, 9 + 1):
            jogada_jogador1()
            if jogada not in range(1, 9 + 1):
                print('Número inválido')

        while jogada == 1 and pos1 == 'ocupado' or \
            jogada == 2 and pos2 == 'ocupado' or \
            jogada == 3 and pos3 == 'ocupado' or \
            jogada == 4 and pos4 == 'ocupado' or \
            jogada == 5 and pos5 == 'ocupado' or \
            jogada == 6 and pos6 == 'ocupado' or \
            jogada == 7 and pos7 == 'ocupado' or \
            jogada == 8 and pos8 == 'ocupado' or \
                jogada == 9 and pos9 == 'ocupado':
            print('Este espaço ja esta ocupado!!')
            verifica_jogador_ocupado()


    def atualizar_jogadas_jogador1():
        global jogada
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        if jogada == 1:
            p1 = jogador
            pos1 = 'ocupado'
        elif jogada == 2:
            p2 = jogador
            pos2 = 'ocupado'
        elif jogada == 3:
            p3 = jogador
            pos3 = 'ocupado'
        elif jogada == 4:
            p4 = jogador
            pos4 = 'ocupado'
        elif jogada == 5:
            p5 = jogador
            pos5 = 'ocupado'
        elif jogada == 6:
            p6 = jogador
            pos6 = 'ocupado'
        elif jogada == 7:
            p7 = jogador
            pos7 = 'ocupado'
        elif jogada == 8:
            p8 = jogador
            pos8 = 'ocupado'
        elif jogada == 9:
            p9 = jogador
            pos9 = 'ocupado'


    def jogadas_maquina():
        global jogada_maquina, maquina
        global p1, p2, p3, p4, p5, p6, p7, p8, p9
        global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9

        print('Deixe - me pensar em uma jogada...')
        sleep(1.5)
        jogada_maquina = randint(1, 9)

        while jogada_maquina == 1 and pos1 == 'ocupado' or \
            jogada_maquina == 2 and pos2 == 'ocupado' or \
            jogada_maquina == 3 and pos3 == 'ocupado' or \
            jogada_maquina == 4 and pos4 == 'ocupado' or \
            jogada_maquina == 5 and pos5 == 'ocupado' or \
            jogada_maquina == 6 and pos6 == 'ocupado' or \
            jogada_maquina == 7 and pos7 == 'ocupado' or \
            jogada_maquina == 8 and pos8 == 'ocupado' or \
                jogada_maquina == 9 and pos9 == 'ocupado':
            jogada_maquina = randint(1, 9)
        print(f'Eu joguei na posição: {jogada_maquina}')

        if jogada_maquina == 1:
            p1 = maquina
            pos1 = 'ocupado'
        elif jogada_maquina == 2:
            p2 = maquina
            pos2 = 'ocupado'
        elif jogada_maquina == 3:
            p3 = maquina
            pos3 = 'ocupado'
        elif jogada_maquina == 4:
            p4 = maquina
            pos4 = 'ocupado'
        elif jogada_maquina == 5:
            p5 = maquina
            pos5 = 'ocupado'
        elif jogada_maquina == 6:
            p6 = maquina
            pos6 = 'ocupado'
        elif jogada_maquina == 7:
            p7 = maquina
            pos7 = 'ocupado'
        elif jogada_maquina == 8:
            p8 = maquina
            pos8 = 'ocupado'
        elif jogada_maquina == 9:
            p9 = maquina
            pos9 = 'ocupado'


    def checar_vencedor():
        global jogador, maquina, turnos, vencedor, pts_jogador, pts_maquina
        global p1, p2, p3, p4, p5, p6, p7, p8, p9

        if p1 == jogador and p2 == jogador and p3 == jogador or \
           p1 == jogador and p5 == jogador and p9 == jogador or \
           p1 == jogador and p4 == jogador and p7 == jogador or \
           p2 == jogador and p5 == jogador and p8 == jogador or \
           p3 == jogador and p6 == jogador and p9 == jogador or \
           p3 == jogador and p5 == jogador and p7 == jogador or \
           p4 == jogador and p5 == jogador and p6 == jogador or \
           p7 == jogador and p8 == jogador and p9 == jogador:
            print('HUMANO WIN')
            pts_jogador += 1
            vencedor = 'EU'
            turnos = 10

        if p1 == maquina and p2 == maquina and p3 == maquina or \
                p1 == maquina and p4 == maquina and p7 == maquina or \
                p1 == maquina and p5 == maquina and p9 == maquina or \
                p2 == maquina and p5 == maquina and p8 == maquina or \
                p3 == maquina and p5 == maquina and p7 == maquina or \
                p3 == maquina and p6 == maquina and p9 == maquina or \
                p4 == maquina and p5 == maquina and p6 == maquina or \
                p7 == maquina and p8 == maquina and p9 == maquina:
            print('EU GANHEI!\n')
            pts_maquina += 1
            vencedor = 'PC'
            turnos = 10


    def atualizartudo():
        global jogada
        global turnos
        global vencedor
        global velha

        if primeiro == 'EU':
            verifica_jogador_ocupado()
            atualizar_jogadas_jogador1()
            atualizar_tabuleiro()
            checar_vencedor()

            if turnos == 5:
                print('DEU VELHA!!')
                turnos = 10
                vencedor = 'EMPATE'
                velha += 1

            if vencedor == '':
                jogadas_maquina()
                atualizar_tabuleiro()
                checar_vencedor()

        elif primeiro == 'PC':
            jogadas_maquina()
            atualizar_tabuleiro()
            checar_vencedor()

            if turnos == 5:
                print('DEU VELHA!!')
                turnos = 10
                vencedor = 'EMPATE'
                velha += 1

            if vencedor == '':
                verifica_jogador_ocupado()
                atualizar_jogadas_jogador1()
                atualizar_tabuleiro()
                checar_vencedor()
        jogada = 0
        turnos += 1


    while turnos <= 5:
        atualizartudo()

    print('-------------- PLACAR --------------')
    print(f'Você: {pts_jogador} | Computador: {pts_maquina} | Velha: {velha}')
    print('------------------------------------')

    while True:
        reiniciar = input('\nQuer jogar de novo? Digite S para sim ou N para não: ').strip().lower()

        if reiniciar in ('s', 'n', 's', 'n'):
            break
        print('\nResposta inválida!')

    if reiniciar == 's' or reiniciar == 's':
        print('\n-----------------------------------------------------')
        continue
    else:
        break



















