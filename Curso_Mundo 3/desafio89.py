listaPS = list()
listaTemp = list()
escolha = ''
while escolha != 'N':
    print('-='*60)
    nome = str(input('Nome: '))
    listaTemp.append(nome)
    n1 = float(input('Nota 1: '))
    listaTemp.append(n1)
    n2 = float(input('Nota 2: '))
    listaTemp.append(n2)
    listaPS.append(listaTemp[:])
    listaTemp.clear()
    print('-='*60)
    escolha = str(input('Deseja continuar inserindo? [S/N] ')).strip().upper()
print('Número      -       Nome      -       Média')
print('\n','-'*60)
for c,n in enumerate(listaPS):
    print(f'{c:^6}{n[0]:>10}{n[1]+n[2]/2:>20}')
print('\n','-'*60)
while True:
    escolher = int(input('Deseja ver notas de qual aluno? (999 para interromper) escreva o número escrito na tabela: '))
    if escolher == 999:
        break
    print(f'\nNota 1 = {listaPS[escolher][1]}\nNota 2 = {listaPS[escolher][2]}')
print('Fim')