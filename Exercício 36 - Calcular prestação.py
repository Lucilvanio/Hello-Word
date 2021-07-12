v1 = float(input('\033[34mValor do imóvel: '))
v2 = float(input('\33[34mSalário do comprador: '))
v3 = int(input('\033[34mAnos de financiamento: '))
r = v1/(v3*12)
if r >= (v2*30)/100:
    print('Infelizmente seu financiamento não foi aprovado!!!')
elif r <= (v2*30)/100:
    print(f'Parabéns, seu financiamento de \033[32mR$ {v1:.2f}\033[m foi aprovado\n'
          f'e suas prestações serão de até \033[32mR$ {r:.2f}\033[m!!!')