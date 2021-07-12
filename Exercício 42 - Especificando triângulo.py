t1 = float(input('Primeiro lado: '))
t2 = float(input('Segundo lado: '))
t3 = float(input('Terceiro lado: '))
if t1 + t2 < t3 or t1 + t3 < t2 or t2 + t3 < t1:
    print('Não pode ser um triângulo')
elif t1 == t2 == t3:
    print(f'É um triângulo Equilátero.')
elif t1 != t2 != t3 != t1: # Lembrar que o programa aceita a conta direta sem or ou and.
    print('É um triângulo Escaleno.')
else:
    print('É um triângulo Isósceles')