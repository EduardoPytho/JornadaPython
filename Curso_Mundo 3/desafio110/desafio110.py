from time import sleep
from moedas4 import resumo
ask = float(input('Digite o valor: R$'))
percentaum = int(input('Digite a porcentagem de aumento (obrigatório): '))
percentred = int(input('Digite a porcentagem de redução (obrigatório): '))
print('-='*30)
sleep(1)
resumo(ask,percentaum,percentred)