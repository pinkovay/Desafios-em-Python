sexo = 0
nome = str(input('Qual o seu nome? ')).capitalize()
while sexo != 'M' and sexo != 'F':
    sexo = str(input(f'Ok {nome}, qual é o seu sexo? [M/F]: ')).upper().strip()
    if sexo == 'M' or sexo == 'F':
        if sexo == 'M':
            print('Sexo Masculino registrado!')
        if sexo == 'F':
            print('Sexo Feminino registrado!')
    else:
        print('Só reconhecemos sexo Masculino ou Feminino, digite algo válido.')
print('Programa chegou ao final.')



