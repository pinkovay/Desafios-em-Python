frase = str(input('Digite algo: ')).upper().strip()
palavras = frase.split()
junto = ''.join(palavras) #através desse comando, as palavras se juntam
invert = junto[::-1]
print(f'{frase} de trás pra frente fica: {invert}')
if junto == invert:
    print('É um palíndromo')
else:
    print('Não é um palíndromo')
