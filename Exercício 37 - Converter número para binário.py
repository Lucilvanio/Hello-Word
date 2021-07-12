a = int(input('Digite um número: '))
print('+=++=++=+ \033[34mEscolha uma base de conversão\33[m +=++=++=+')
print('[1] Binário\n[2] Octal \n[3] Hexadecimal')
b = int(input('Opção:  '))
bn = bin(a)
oc = oct(a)
he = hex(a)
if b == 1:
    print(f'O número {a} Convertido para Binário é {bn[2:]}') # O [2:} é para não aparecer os dois primeiros números.
elif b == 2:
    print(f'O numero {a} Convertido para Octal é {oc[2:]}')
elif b == 3:
    print(f'O número {a} Convertido para Hexadecimal é {he[2:]}')
else:
    print(f'{b} Não é uma escolha válida.')

