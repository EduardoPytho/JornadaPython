from moedas2 import *
ask = float(input('Digite o valor: R$'))
percent = int(input('Digite a porcentagem (obrigatório): '))
print('-='*30)
print(f'A metado do valor {moeda(ask)} é {moeda(metade(ask))}')
print('-='*30)
print(f'O dobro do valor {moeda(ask)} é {moeda(dobro(ask))}')
print('-='*30)
print(f'Aumentando em {percent}%, o valor {moeda(ask)} é {moeda(aumentar(ask,percent))}')
print('-='*30)
print(f'Diminuindo em {percent}%, o valor {moeda(ask)} é {moeda(diminuir(ask,percent))}')