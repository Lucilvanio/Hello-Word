vl = int(input('Velocidade aferida: '))
if vl == 80:
    print('Parabéns, você está dentro do limite de velocidade.')
else:
    print(f'O limite de velocidade é de 80 km/h, você estava a {vl}km/h e foi multado em R$ {(vl-80)*7:.2f}.')