import random
a = ('Pedra', 'Papel', 'Tesoura')
b = random.randint(0, 2)
c = int(input('Escolha uma opção: '))
print('''
[0] Pedra
[1] Papel
[2] Tesoura''') # 3 aspas para passar as palavras para baixo usando enter em um mesmo print.
print(f'Você jogou {a[c]} e eu {a[b]}') # <- Lembrar dessa atribuição de {a[c]} que atribui a lista ao random.
if b == 0:
    if c == 0:
        print('Empatou')
    elif c == 1:
        print('Você ganhou!!!')
    elif c == 2:
        print('Eu Ganhei!!!')
    else:
        print('Jogada inválida')
elif b == 1:
    if c == 1:
        print('Empatou')
    elif c == 2:
        print('Você ganhou!!!')
    elif c == 0:
        print('Eu Ganhei!!!')
    else:
        print('Jogada inválida')
elif b == 2:
    if c == 2:
        print('Empatou')
    elif c == 0:
        print('Você ganhou!!!')
    elif c == 1:
        print('Eu Ganhei!!!')
    else:
        print('Jogada inválida')