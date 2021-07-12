p1 = float(input('Preço do produto: '))
print('[1] Débito\n[2]Crédito a vista\n[3]Parcelado ')
a1 = int(input('Forma de pagamento: '))
if a1 == 1:
    print(f'O valor a vista com desconto fica  \033[32mR$ {p1-(p1*10/100):.2f}\033[m.')
elif a1 == 2:
    print(f'O Valor o crédito a vista ou débito fica \033[32mR$ {p1 - (p1*5/100):.2f}\033[m.')
elif a1 > 3:
    print('\033[31mForma de pagamento não encontrada, entre em contato  com o administrador.')
else:
    a2 = int(input('Quantidade de parcelas: '))
    if a2 >2:
        print(f'O valor parcelado fica {a2}X de \033[32mR$ {(p1+(p1*20/ 100))/a2:.2f}\033[m.')
    elif a2 <= 2:
        print(f'Para pagamento no crédito em {a2}x o valor é o mesmo ')