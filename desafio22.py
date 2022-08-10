#revisar bastante esse
nome = input('Qual o seu nome? ')
maius = nome.upper()
print(f'Olha como fica seu nome todos com letras grandes: {maius}')
minus = nome.lower()
print(f'Agora todo em letras pequenas: {minus}')
a1 = nome.split()
a2 = (''.join(a1))
a3 = len(nome)
print(f'Seu nome contém {a3} letras')
b0 = nome.split()
b1 = b0[0]
b2 = len(b1)
print(f'E seu primeiro nome tem apenas {b2} letras')
