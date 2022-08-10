import datetime
year = datetime.date.today().year


def voto(birth):
    global nome
    age = year - birth
    if age <= 15:
        print(f'{nome}, Você não está autorizado a votar.')
        print(f'Você só tem {age} anos.')
    elif 16 <= age < 18 or age >= 65:
        print(f'{nome} seu voto é opcional.')
        if age >= 65:
            print(f'Com 65 anos se torna opcional, você tem {age} anos.')
        else:
            print(f'Com {age} anos ainda é opcional.')
    else:
        print(f'{nome} seu voto é obrigatório.')
        print(f'Você já tem {age} anos!!!')


print('-=' * 30)
print(f"{'APROVAÇÃO PARA VOTAÇÃO':~^60}")
print('-=' * 30)
print()
nome = str(input('Nome: ')).strip().capitalize()
birth = int(input('Ano de nascimento: '))
voto(birth)
