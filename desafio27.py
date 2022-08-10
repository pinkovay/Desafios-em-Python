#bem útil o -1, com o uso do len
nome = str(input('Qual seu nome? ')).strip()
divisao = nome.split()
print('Muito bonito seu nome', divisao[0])
print('E', divisao[len(nome)-1], 'é muito lindo também!!')
