from datetime import date
a = int(input('Ano de Nascimento: '))
a1 = date.today().year - a
if a1 <= 9:
    print(f'Você tem \033[34m{a1}\033[m anos e está na categoria \033[34mMIRIM.')
elif a1 <= 14:
    print(f'Você tem \033[34m{a1}\033[m anos e está na categoria \033[34mINFANTIL.')
elif a1 <= 19:
    print(f'Você tem \033[34m{a1}\033[m anos e está na categoria \033[34mJUNIOR.')
elif a1 <= 20:
    print(f'Você tem \033[34m{a1}\033[m anos e está na categoria \033[34mSÊNIOR.')
else:
    print(f'Você tem \033[34m{a1}\033[m anos e está na categoria \033[34mMASTER.')