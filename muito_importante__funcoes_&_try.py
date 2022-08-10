dice = list()
finaly_dice = list()

#este é o arquivo mais importante para mim, certamente voltarei muitas vezes

def readmoney(msg):
    '''lido = False
    while not lido:
        entrada = (str(input(msg))).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '' or entrada.isalnum() or len(entrada) == 1 and entrada == ',' or entrada == '.':
            print(f'Preço inválido.')
        else:
            return float(entrada)'''

    while True:
        valor = input(msg)
        if valor.replace('.', '').replace(',', '').isdigit() and valor.count('.') < 2 and valor.count(',') < 2:
            return float(valor.replace(',', '.'))
        print(f'ERRO: "{valor}" é um preço inválido!')


def coin(n):
    return f'R${n}'


def double(n, c=False):
    if c:
        return coin(n * 2)

    return n * 2


def half(n, c=False):
    if c:
        return coin(n / 2)
    return n / 2


def increase(n, a=0, c=False):
    if c:
        return coin(((a / 100) * n) + n)
    return ((a / 100) * n) + n


def reduce(n, a=0, c=False):
    if c:
        return coin(n - ((a / 100) * n))
    return n - ((a / 100) * n)

def um():
    '''while 1:
          dice = input(msg).strip().replace(' ', '')
          if dice.isnumeric():
              print(f'Você digitou o número inteiro > {int(dice)}')
          else:
              print(f'\033[31m{dice.capitalize()} Não é um número inteiro.\033[m')'''


#___________OUTRO ARQUIVO__________

from desafio111.utilidadesCev import dado


def resumo(n, a=0, b=0):
    print('-' * 30)
    print('RESUMO DO VALOR'.center(30))
    print('-' * 30)
    print(f'Valor analisado: \t{(dado.coin(n))}')
    print(f'Dobro do valor: \t{(dado.double(n, True))}')
    print(f'Metade do valor: \t{(dado.half(n, True))}')
    print(f'{a}% de aumento: \t{(dado.increase(n, a, True))}')
    print(f'{b}% de redução: \t{(dado.reduce(n, b, True))}')
