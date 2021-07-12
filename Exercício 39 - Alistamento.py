from datetime import date
a1 = int(input('Ano de nascimento: '))
a2 = date.today().year - a1
if a2 == 17:
    print(f'Falta \033[32m{18 - a2}\033[m ano para você se alistar.')
elif a2 < 18 and a2 !=17:
    print(f'Faltam \033[32m{18 - a2}\033[m anos para você se alistar.')
elif a2 == 18:
    print(f'Você completou \033[32m18\033[m anos e já pode se alistar.')
else:
    print(f'Você passou \033[32m{a2 - 18}\033[m anos do alistamento.')