v = float(input('valor Metros: '))
v1 = int(input('Km/h: '))
mt = v1/1.609
nm = v1/1.852
c = v*100
m = c*10 # Ou pode multiplicar o v*1000 da o mesmo resultado.
print(f'\033[32m{v}\033[m Metros convertido para \ncentímetros é \033[32m{c}\033[m e para \nmilímetros é \033[32m{m}\033[m')
print(f'{v1} km equivale a {mt:.2f} Milhas terrestres e a {nm:.2f} Milhas náuticas.')
