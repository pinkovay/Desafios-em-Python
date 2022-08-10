import turtle; import random; from time import sleep
numeros = list()

def Sorteio():
    for c in range(0, 5):
        nu = random.randint(0, 100)
        if nu not in numeros:
            numeros.append(nu)
    print(numeros)

def Soma_par():
    par = 0
    for num in numeros:
        if num % 2 == 0:
            par += num
    print(f'A soma de todos os números pares digitados é: {par}')
    print('_' * 40)
    print('FORMANDO O CIRCULO:')
    sleep(2)
    circulo = turtle.Turtle()
    circulo.penup()
    circulo.forward(10)
    circulo.left(10)
    circulo.pendown()
    circulo.circle(par)


Sorteio(), Soma_par()



