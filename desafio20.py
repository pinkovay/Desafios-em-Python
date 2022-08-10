import random
al1 = str(input('Primeiro aluno(a): '))
al2 = str(input('Segundo aluno(a): '))
al3 = str(input('Terceiro aluno(a): '))
al4 = str(input('Quarto aluno(a): '))
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print(f'A ordem é {lista}')
