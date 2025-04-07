def metade(num=10.5):
    return num/2
def aumentar(num=100.99,porcent=50):
    return num + ((num * porcent) / 100)
def diminuir(num=100.99,percent=80):
    return num - ((num * percent) / 100)
def dobro(num=47.99):
        return num * 2
def moeda(valor=100.99,moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.',',')