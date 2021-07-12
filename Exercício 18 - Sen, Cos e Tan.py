from math import sin, cos, tan, radians
a = int(input('Digite um ângulo: '))
#sin = math.sin(math.radians(a))               <=
#cos = math.cos(math.radians(a))               <= Também funciona dessa forma.
#tan = math.tan(math.radians(a))               <=
print(f'O seno é \033[4;35m{sin(radians(a)):.2f}\033[m \n'
      f'cosseno  \033[4;35m{cos(radians(a)):.2f}\033[m \n'
      f'tangente \033[4;35m{tan(radians(a)):.2f}')

