def metade(num=10.5,convert=True):
    if convert:
        return moeda(num/2)
    else:
        return num/2
def aumentar(num=100.99,porcent=50,convert=True):
    if convert:
        return moeda(num + ((num * porcent) / 100))
    else:
        return num + ((num * porcent) / 100)
def diminuir(num=100.99,percent=80,convert=True):
    if convert:
        return moeda(num - ((num * percent) / 100))
    else:
        return num + ((num * percent) / 100)
def dobro(num=47.99,convert=True):
    if convert:
        return moeda(num*2)
    else:
        return num*2
def moeda(valor=100.99,moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')
def resumo(valor=100,aumento=80,reducao=35):
    print('-' * 30)
    print(f'{"RESUMO DO VALOR":^30}')
    print('-' * 30)
    print(f'Preço analisado: \t{moeda(valor)}')
    print(f'Dobro do preço: \t{dobro(valor)}')
    print(f'Metade do preço: \t{metade(valor)}')
    print(f'{aumento}% de aumento: \t{aumentar(valor,aumento)}')
    print(f'{reducao}% de redução: \t{diminuir(valor,reducao)}')
    print('-'*30)