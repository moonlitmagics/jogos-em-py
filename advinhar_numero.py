import random

def jogo_advinhacao():
    numero_secreto = random.randint(1, 50)
    tentativas = 0

    print('Bem_vindo ao jogo de advinhação!')
    print('Estou pensando em um número de 1 a 50')

    while True:
        palpite = input('Digite o seu palpite: ')

        if not palpite.isdigit():
            print('Por favor, digite um número válido.')
            continue
        palpite = int(palpite)
        tentativas += 1

        if palpite < numero_secreto:
            print('Muito baixo!')
        elif palpite > numero_secreto:
            print('Muito alto!')
        else: 
            print(f'Parabéns! Você acertou o número em {tentativas} tentativas. ')
            break
if __name__ == "__main__":
    jogo_advinhacao()