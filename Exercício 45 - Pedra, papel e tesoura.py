import random
pe = str('Pedra')
pa = str('Papel')
te = str('Tesoura')
print('[1]PEDRA\n[2]PAPEL\n[3]TESOURA')
a1 = int(input('Escolha pedra, papel ou tesoura: '))
list = [pe, pa, te]
r = random.choice(list)
if a1 == 1 and r == pe:
    print(f'Você escolheu {pe} e eu {r}, empatamos!!! ')
elif a1 == 3 and r == te:
    print(f'Você escolheu {te} e eu {r}, empatamos!!! ')
elif a1 == 2 and r == pa:
    print(f'Você escolheu {pa} e eu {r}, empatamos!!! ')
elif a1 == 1 and r == pa:
    print(f'Você escolheu {pe} e eu {r}, eu ganhei!!! ')
elif a1 == 2 and r == te:
    print(f'Você escolheu {pa} e eu {r}, eu ganhei!!! ')
elif a1 == 3 and r == pe:
    print(f'Você escolheu {te} e eu {r}, eu ganhei!!! ')
elif a1 == 1 and r == te:
    print(f'Você escolheu {pe} e eu {r}, Você ganhou!!! ')
elif a1 == 2 and r == pe:
    print(f'Você escolheu {pa} e eu {r}, Você ganhou!!! ')
elif a1 == 3 and r == pa:
    print(f'Você escolheu {te} e eu {r}, Você ganhou!!! ')