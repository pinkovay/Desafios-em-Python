from time import sleep

def contador(a, b, c):
    if b > a or c < 0:
        for f in range(a, b, c):
            print(f, end=' ')
            sleep(0.5)
        print()
    elif b < a:
        if c >= 0:
            for f in range(a, b, -c):
                print(f, end=' ')
                sleep(0.5)
        print()

def mostrarlinha():
    print('_' * 30)


mostrarlinha()
print('Contando de 1 até 10')
for c in range(1, 11):
    print(c, end=' ')
    sleep(0.5)
print()
mostrarlinha()
print('Contando de 10 a 0, pulando de 2 em 2')
for c in range(10, -1, - 2):
    print(c, end=' ')
    sleep(0.5)
print()
mostrarlinha()
print('Agora é sua vez de personalizar a contagem')
a = int(input('Inicio: '))
b = int(input('Fim: '))
c = int(input('Intervalo: '))
if c == 0:
    c += 1
b -= 1
contador(a, b, c), mostrarlinha()
