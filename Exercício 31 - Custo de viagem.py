v1 = int(input('Distancia da viagem: '))
if v1 <= 200:
    print(f'O valor de sua passagem é de: R$ {v1*.50:.2f}')
else:
    print(f'O valor da passagem é de R$ {v1*.45:.2f}')