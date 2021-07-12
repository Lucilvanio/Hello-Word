import math
n1 = float(input('Digite um número: '))
r = n1**(1/2)
print(f'A raiz do número {n1:.2f} formatado fica {math.ceil(r):.2f} arredondado para cima e arredondado para baixo {math.floor(r):.2f}')
