from time import sleep
cores = {'verde':'\033[0;32m','verden':'\033[1;32m','amarelo':'\033[1;33m','roxo':'\033[1;35m','vermelhon':'\033[1;31m','vermelho':'\033[0;31m','azul':'\033[1;34m','fecham':'\033[m'}
casa = float(input(f'Qual o valor da {cores["roxo"]}casa?{cores["fecham"]}{cores["verde"]} R$'))
sleep(0.3)
sl = float(input(f'{cores["fecham"]}Qual o seu {cores["roxo"]}salário?{cores["fecham"]}{cores["verde"]} R$'))
sleep(0.3)
ano = int(input(f'{cores["fecham"]}Em {cores["roxo"]}quantos anos{cores["fecham"]} quer pagar?'))
sleep(0.3)
ano = ano*12
calculo = casa / ano
pt = sl*30/100
if calculo >= pt:
    print(f'{cores["vermelho"]}Solicitação de empréstico negado,o pagamento mensal custa mais de 30% de seu salário. ({calculo:.2f}){cores["fecham"]}')
else:
 print(f'{cores["verden"]}Empréstimo feito com sucesso! será cobrado mensalmente "{calculo:.2f}" Reais.')