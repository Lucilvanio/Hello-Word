v1 = float(input('1º lado do triângulo: '))
v2 = float(input('2ª lado do triângulo: '))
v3 = float(input('3ª lado do triângulo: '))
if v1 < v2 + v3 and v2 < v1 + v3 and v3 < v1 + v2:
    print('Pode ser um triângulo.')
else:
    print('Não pode ser um triângulo.')