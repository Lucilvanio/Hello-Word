n = int(input('Digite um número entre 0 e 9999: '))
m = n // 1000 % 100
c = n // 100 % 10
d = n // 10 % 10
u = n // 1 % 10
if m == 1:
    print(f'Você tem {m} milhar\n{c} centena\n{d} dezenas\n{u} unidades')
else:
    print(f'Você tem {m} milhares\n{c} centenas\n{d} dezenas\n{u} unidades')
    if m and c == 1:
        print(f'Você tem {m} milhar\n{c} centena\n{d} dezenas\n{u} unidades')
    else:
        print(f'Você tem {m} milhares\n{c} centenas\n{d} dezenas\n{u} unidades')
if m and c and d == 1:
    print(f'Você tem {m} milhar\n{c} centena\n{d} dezena\n{u} unidades')
else:
    print(f'Você tem {m} milhares\n{c} centenas\n{d} dezenas\n{u} unidades')