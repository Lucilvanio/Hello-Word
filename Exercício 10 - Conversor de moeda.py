r = float(input('Quantos reais você deseja trocar? R$ '))
c = r/5.27
b = r*1.31
print('')
print(f'Com \033[34mR$ {r}\033[m '
      f'você pode comprar:'
      f'\n\033[34mU$ {c:.2f}\033[m Dólares e '
      f'\033[34mBO {b:.2f}\033[m Pesos Bolivianos.')