print('PROGRAMA CRIADO PARA CALCULAR MÉDIA DO ALUNO (ATÉ 3 NOTAS POR ENQUANTO)')
nota1 = float(input('Primeira nota: '))
nota2 = float(input('Segunda nota: '))
nota3 = float(input('Terceira nota: '))
media = (nota1 + nota2 + nota3) / 3
if media < 5.0:
    print(f'A média do aluno é: {media}')
    print(f'Aluno REPROVADO.')
elif media > 5.0 and media < 7.0:
    print(F'A média do aluno é: {media}')
    print('Aluno em RECUPERAÇÃO.')
elif media >= 7.0:
    print(f'A média do aluno é: {media}')
    print('Aluno APROVADO.')
else:
    print('ERRO.')
