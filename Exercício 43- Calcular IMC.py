p1 = float(input('Digite o seu peso: Kg '))
a1 = float(input('Digite sua altura: '))
imc = p1/(a1**2) # Também pode elevar ao quadrado usando a1*a1, o resultado é o mesmo.
if imc < 18.5:
    print(f'Seu IMC é de \033[34m{imc:.2f}\033[m, você está abaixo do peso.')
elif imc <= 24.9:
    print(f'Seu IMC é de \033[34m{imc:.2f}\033[m, seu peso está normal.')
elif imc <= 29.9:
    print(f'Seu IMC é de \033[34m{imc:.2f}\033[m, você está com sobrepeso.')
elif imc <= 39.9:
    print(f'Seu IMC é de \033[34m{imc:.2f}\033[m, você está com obesidade.')
else:
    print(f'Seu IMC  é de \033[34m{imc:.2f}\033[m, você está com obesidade grave.')