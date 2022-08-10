def Fatorial(num, show=False):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    if show:
        for c in range(num, 0, -1):
            if c == 1:
                print(f'1 = {f}')
            else:
                print(f'{c} x ', end='')
    else:
        return f


print(Fatorial(5, show=True))

