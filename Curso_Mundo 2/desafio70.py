total = mais_de_1000 = contador = produto_mais_baraton = 0
produto_mais_barato = ''
while True:
    contador += 1
    print('-'*30,end=' ')
    print(f'\033[1;31m{contador}° PRODUTO\033[m',end=' ')
    print('-'*30)
    print('-='*40)
    nome = str(input('Insira o nome do produto: \033[0;33m'))
    print('\033[m-='*40)
    preço = float(input('\033[mInsira o preço do produto: \033[0;32mR$'))
    total += preço
    if preço >1000:
        mais_de_1000 += 1
    if contador == 1:
        produto_mais_barato = nome
        produto_mais_baraton = preço
    elif contador >1 and preço<produto_mais_baraton:
        produto_mais_barato = nome
        produto_mais_baraton = preço
    print('\033[m-='*40)
    escolha = str(input('Deseja continuar inserindo produtos? [S/N]: ')).strip().upper()
    if escolha != 'S' and escolha != 'N':
        while escolha != 'S' and escolha != 'N':
            escolha = str(input('Insira uma escolha válida. [S/N]: ')).strip().upper()
    if escolha == 'N':
        break
print(f'\n\033[1;35mO total gasto nas compras é R${total:.2f}.')
print(f'\n{mais_de_1000} produto(s) custam mais de 1000 Reais.')
print(f'\nO produto mais barato do carrinho é o {produto_mais_barato}\033[m')
