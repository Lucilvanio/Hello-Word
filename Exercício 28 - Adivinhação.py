import random
import time
n = int(input('Adivinhe em que número estou pensando de 1 a 5: '))
l = random.randint(1, 5) # em .randint basta colocar o primeiro e o ultimoo numero, ex: 1, 5 sorteará um numero entre 1 e 5.
print('PROCESSANDO...')
time.sleep(1.5)
if n == l:
    print('Acertô Mizeraaaaavi!!!')
else:
    print(f'Você errou abestado, não pensei no número {n} pensei no número {l}')