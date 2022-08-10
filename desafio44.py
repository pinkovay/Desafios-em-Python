valor = float(input('Qual o preço do produto? R$'))
print('[FORMAS DE PAGAMENTO]')
print('[1]À vista dinheiro/cheque\n[2]À vista no cartâo\n[3]Em até 2x no cartão: preço formal\n[4]3x ou mais no cartão: 20% de juros')
con = int(input('Sua escolha: '))
print('==' * 40)
if con == 1:
    desconto1 = valor * 10 / 100
    desconto2 = valor - desconto1
    print(f'Sua compra sairá por R${desconto2}')
elif con == 2:
    desconto1 = valor * 5 / 100
    desconto2 = valor - desconto1
    print(f'Sua compra sairá por R${desconto2}')
elif con == 3:
    duasvezes = valor / 2
    print(f'Será pago em duas parcelas, de R${duasvezes} cada.')
elif con == 4:
    parcela = float(input('Ok, desejar pagar em quantas vezes? '))
    if parcela == 2:
        print('Indicamos que use a opção 3 então, reinicie o programa.')
    else:
        juros = valor * 20 / 100
        juros2 = (juros + valor) / parcela
        print(f'Cada parcela será de R${juros2}')
else:
    print('Digite algo válido, reinicie o programa.')


'''à vista dinheiro/cheque: 10% de desconto

– à vista no cartão: 5% de desconto

– em até 2x no cartão: preço formal 

– 3x ou mais no cartão: 20% de juros'''