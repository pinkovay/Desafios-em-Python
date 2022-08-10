print('Programa destinado a calcular quantos litros de tinta serão usados para pintar uma parede')
alt = float(input("Diga a altura da parede em metros:"))
lar = float(input('Agora a largura:'))
area = alt * lar
mls = area / 2.0
print(f'Serão usados {mls} litros de tinta:')
