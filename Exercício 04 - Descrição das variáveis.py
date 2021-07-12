a = input('\033[32mDigite um nome: ')
b = int(input('Digite um número:'))
print('O tipo primitivo é:  ', type(a))
print('São letras?', a.isalpha())
print('São números?', a.isnumeric())
print('São numeros  letras?', a.isalnum())
print('É maiusculo?', a.isupper())
print('É minusculo?', a.islower())
print('Tipo primitivo', type(b))
print('Começa com maiuscula?', a.istitle())
print('a vingança nunca é plena, mata a lama e a envenena!!!'.capitalize())
#   Usar "capitalize" para captalizar e deixar a primeira letra da frase em maiúsculo.
#   "title" deixa a primeira letra de todas as palavras em maiúsculo.