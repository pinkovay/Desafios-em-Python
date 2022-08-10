c = ("\033[m",  # 0 - Sem cor
     '\033[30;41m',  # 1 - Vermelho
     '\033[30;42m',  # 2 - verde
     '\033[30;43m',  # 3 - amarelo
     '\033[30;44m',  # 4 - azul
     '\033[30;45m',  # 5 - roxo
     '\033[7;30',  # 6 - branco
     )


def ajuda(com):
    Titulo(f'Acessando manual do comando \'{com}\'', 4)
    print(c[2], end='')
    help(com)
    print(c[0], end='')


def Titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')


comando = ''
while True:
    Titulo("SISTEMA DE AJUDA PYHELP", 3)
    comando = str(input('Função ou Biblioteca: '))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
Titulo("ATÉ LOGO", 1)
