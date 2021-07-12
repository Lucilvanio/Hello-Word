n1 = float(input('Digite o salário: '))
if n1 <= 1250:
    print(f'Seu aumento é de 15%, seu novo salário é R$ {(n1*15/100)+n1:.2f}.')
else:
    print(f'Seu aumento é de 10%, seu novo salário é R$ {(n1*10/100)+n1:.2f}.')