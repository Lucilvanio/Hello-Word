a = int(input('Digite um ano: '))
if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'O ano {a} é um ano bissexto.')
else:
    print(f'o ano {a} não é um ano bissexto.')
