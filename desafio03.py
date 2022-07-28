n1 = int(input('Fale um número: '))
n2 = int(input('Certo, agora diga outro: '))
var = n1 + n2
print('Se somarmos {} com {}, seu resultado será {}'.format(n1, n2, var))
print('And your type is {}'.format(type(var)))

soma = 0
for c in range(2):
    num = float(input('Digite um número: '))
    soma += num
print(soma)