cores = {'verde':'\033[0;32m','verden':'\033[1;32m','amarelo':'\033[0;33m','amarelon':'\033[1;33m','roxo':'\033[1;35m','vermelhon':'\033[1;31m','vermelho':'\033[0;31m','azul':'\033[1;34m','fecham':'\033[m'}

from time import sleep

n1 = int(input(f'{cores["amarelo"]}Digite um número qualquer: '))

n2 = int(input(f'{cores["amarelo"]}Digite outro número qualquer novamente: '))

print(f'{cores["roxo"]}Processando..')

sleep(0.5)

if n1>n2:
    print(f'{cores["verde"]}O primeiro valor é maior que o segundo valor.\n')
elif n2>n1:
    print(f'{cores["verde"]}O segundo valor é maior que o primeiro valor.\n')
else:
    print(f'{cores["vermelhon"]}Não existe valor menor, Os dois são iguais.\033[m\n')
