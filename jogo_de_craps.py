from random import randint

def jogar_dado():
     dado = randint(2,13)
     return dado

def primeira_jogada():
    if dado == 7 or dado == 11:
        return 'n'
    
    if dado == 2 or dado == 3 or dado == 12:
        return 'c'
    
    if dado == 4 or dado == 5 or dado == 6 or dado == 8 or dado == 9 or dado == 11:
        return dado

def segunda_jogada():
    if dado == 7:
        return 'c'
    if dado == guardar:
        return True




jogada = 0
while True:
    while True:
        jogar = input('Deseja jogar o dado? S/N ').lower()
        jogada += 1
        if jogar == 's':
            dado = jogar_dado()
            print(f'VOCÊ TIROU O NÚMERO {dado} NO DADO!')

            if jogada == 1:
                natural_craps = primeira_jogada()
                if natural_craps == 'n':
                    print('VOCE É UM NATURAL! VOCÊ GANHOU!!!!')

                elif natural_craps == 'c':
                    print('VOCÊ É UM CRAPS! VOCÊ PERDEU!!!!')

                else:
                    print(f'SEU NÚMERO PONTO É {dado}')
                    guardar = dado
            
            if jogada > 1:
                natural_craps=segunda_jogada()
                if natural_craps == 'c':
                    print('VOCE PERDEU!!! jOGO ENCERRADO!')
                if natural_craps == True:
                    print(f'O número {guardar} e {dado} são iguais! VOCE GANHOU!!!!')
            


        if jogar == 'n':
            print('REINICIANDO JOGO')
            break;
    jogar_novamente = input('Deseja jogar novamente? S/N: ').lower()
    if jogar_novamente == 'n':
        print('JOGO ENCERRADO')
        break;

        
    





