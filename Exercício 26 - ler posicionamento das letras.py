n = str('A vingança nunca é plena, mata a alma e a envenena!!! ').lower()
print(f'A frase tem {n.count("a")} letras A')
print(f'A primeira está na posição { n.find("a")+1}')
print(f'e a ultima na posição {n.rfind("a")+1}')