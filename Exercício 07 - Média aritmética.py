n1 = float(input('Primeiro bimestre: '))
n2 = float(input('Segundo bimestre: '))
n3 = float(input('Terceiro bimestre: '))
n4 = float(input('Quarto bimestre: '))
r = (n1+n2+n3+n4)/4
if r >= 7.0:
    print(f'Sua média final é  \033[34m{r}\033[m \nParabéns!!! Você foi aprovado!!!')
else:
    print(f'Sua média final é  \033[31m{r}\033[m \nVocê foi reprovado!!!')