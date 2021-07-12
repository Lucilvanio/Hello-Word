n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))
if n1 > n2:
    print(f'O número \033[34m{n1}\033[m é maior que o número \033[34m{n2}\033[m.')
elif n1 < n2:
    print(f'O número \033[34m{n2}\033[m é maior que o número \033[34m{n1}\033[m.')
else:
    print(f'Os números \033[34m{n1}\033[m e \033[34m{n2}\033[m são iguais.')