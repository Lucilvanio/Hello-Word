import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
#hi = math.hypot(co, ca) Também funciona assim
#print(f'A Hipotenusa é {hi:.2f}.')
print(f'A hipotenusa é {math.hypot(co, ca):.2f}')