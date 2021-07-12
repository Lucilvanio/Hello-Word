import random
a1 = str('Luiz')
a2 = str('Maísa')
a3 = str('Pablo')
a4 = str('Diego')
n1 = [a1, a2, a3, a4]
print(f'O escolhido foi : \033[36m{random.choice(n1)}')