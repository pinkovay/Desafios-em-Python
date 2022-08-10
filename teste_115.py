from desafio115.lib.arquivo import *
from desafio115.lib.sistema import *
from time import sleep

arq = 'cursoemvideo.txt'

if not ArquivoExiste(arq):
    CriarArquivo(arq)


while 1:
    Cabecalho('MENU PRINCIPAL')
    resposta = Menu(['Ver pessoas cadastradas', 'Cadastrar nova pessoa', 'Sair do sistema'])
    if resposta == 1:
        LerArquivo(arq)
    if resposta == 2:
        EscreverArquivo(arq)
    if resposta == 3:
        print(f'\033[31mSaindo do sistema... Até logo!!')
        break
    sleep(1)

