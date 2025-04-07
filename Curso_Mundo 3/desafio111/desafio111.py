from time import sleep
from UtilidadesCeV.Moeda import resumo
from UtilidadesCeV.Dado import moneyreader

ask = moneyreader('Digite o valor: R$')
print('-='*30)
sleep(1)
resumo(ask,45,25)