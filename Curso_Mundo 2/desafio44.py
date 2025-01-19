from time import sleep
nome = input('Qual o nome do produto? NOME:\033[0;33m')
valor = float(input('\033[mQual o valor do produto? R$\033[0;33m'))
print('\033[1;36mProcessando..')
sleep(2)
mp = int(input('\033[0;37mQual a forma de pagamento?\n\033[1;34m1- À vista dinheiro/cheque\n2- À vista no cartão\n3- Parcelar \n\nDigite:\033[0;33m'))
print('\033[1;36mProcessando..')
sleep(2)
if mp >3:
    print('\033[1;31mERRO, Você digitou um número inválido.')
elif mp == 1:
    valor = valor-(valor*10/100)
    print(f'\033[1;32mPagamento do \033[1;32m{nome}\033[1;32m realizado com sucesso!\n\033[0;32mVocê teve 10% de desconto, você irá pagar somente \033[1;32mR${valor:.2f}')
elif mp == 2:
    valor = valor-(valor*5/100)
    print(f'\033[1;32mPagamento do \033[1;32m{nome}\033[1;32m realizado com sucesso!\n\033[0;32mVocê teve 5% de desconto, você irá pagar somente \033[1;32mR${valor:.2f}')
elif mp == 3:
    parcelas = int(input('\033[mEm quantas parcelas? (Limite 24): \033[0;33m'))
    if parcelas >24:
        print('\033[1;31mO limite é 24 vezes.')
    if parcelas == 1:
        print('\033[1;31mParcelar somente uma vez é a mesma coisa que comprar o total.')
    elif parcelas == 2:
        valor = valor/2
        print('\033[1;36mProcessando..')
        sleep(2)
        print(f'\033[1;32mPagamento do \033[1;32m{nome}\033[1;32m realizado com sucesso!\n\033[0;32mVocê irá pagar 2 parcelas de \033[1;32mR${valor:.2f}\033[0;32.\033[m')
    elif parcelas >2 and parcelas <=24:
        valor =float((valor+(valor*20/100))/parcelas)
        print('\033[1;36mProcessando..')
        sleep(2)
        print(f'\033[1;32mPagamento do \033[1;32m{nome}\033[1;32m realizado com sucesso!\n\033[0;32mVocê terá 20% de juros,Você irá pagar {parcelas} parcelas de \033[1;32mR${valor:.2f}\033[0;32.\033[m')