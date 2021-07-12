import time
n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
n3 = float(input('Terceira nota: '))
n4 = float(input('Quarta nota: '))
nf = (n1+n2+n3+n4)/4
print('Aguardando...')
time.sleep(1.5)
if 7 > nf >= 5: # Observar que o nf ficou entre o 7 e o 5 Ex: " if 7> nf >= 5"
    print(f'Sua nota final foi \033[33m{nf:.2f}\033[m e você está de recuperação.')
elif nf < 5:
    print(f'Sua nota final foi de \033[33m{nf}\033[m e você foi reprovado.')
else:
    print(f'Parabéns sua nota final foi de \033[33m{nf}\033[m e você está aprovado!!!')