# Biblioteca
from random import randint

# Charme
print('-=-'*20)
print('PAR OU ÍMPAR')
print('-=-'*20)

# Variáveis Globais
contador = 0
venceu = 0

# Calculando
while True:
    computador = randint(1, 10)
    jogador = int(input('Digite um valor: '))
    resposta = ' '
    total = computador + jogador
    contador += 1
    while resposta not in 'PI':
        resposta = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()
        print('='*30)
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total foi {total}', end='. ')
    if computador % 2 == 0:
        print('Resultado PAR')
    else:
        print('Resultado ÍMPAR')
    if resposta == 'P':
        if total % 2 == 0:
            print('Você venceu!')
            venceu += 1
            print('-'*25)
        elif total % 2 == 1:
            print('Você perdeu!')
            print('-' * 25)
            break
    elif resposta == 'I':
        if total % 2 == 0:
            print('Você perdeu!')
            print('-' * 25)
            break
        elif total % 2 == 1:
            print('Você venceu!')
            venceu += 1
            print('-'*25)
    print('Vamos jogar novamente!')
    print('-'*25)
print(f'Você jogou um total de {contador} vez(s) e venceu {venceu} delas!')
