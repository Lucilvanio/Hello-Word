a = float(input('Altura da parede: '))
l = float(input('Largura da parede: '))
m = a*l
print(f'Sua parede tem \033[35m{m}m²\033[m, você gastará de \033[35m{m/2:.2f}\033[m litros de tinta para pintála.')
