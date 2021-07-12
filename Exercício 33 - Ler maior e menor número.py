n = int(input('Digite um número: '))
n1 = int(input('Digite outro número: '))
n2 = int(input('Digite mais um número: '))
if n < n1 and n < n2:
    print(f'{n} é o menor número.')
if n1 < n and n1 < n2:
    print(f'{n1} é o menor número.')
if n2 < n1 and n2 < n:
    print(f'{n2} é o menor número.')
if n > n1 and n > n2:
    print(f'{n} é o maior número.')
if n1 > n and n1 > n2:
    print(f'{n1} é o maior número.')
if n2 > n and n2 > n1:
    print(f'{n2} é o maior número.')
