
dados = dict()
dados['nome'] = list()
dados['sexo'] = list()
dados['idade'] = list()
contagem = 0
esc = ''
while esc != 'N':
    dados['nome'].append(str(input('Nome: ')).strip().title())
    dados['sexo'].append(str(input('Gênero: ')).strip().upper() [0])
    idade = int(str(input('Idade: ')).strip().split() [0])
    dados['idade'].append(idade)
    contagem += idade
    esc = str(input('Continuar? [S/N] ')).strip().upper()[0]
média = (contagem/len(dados['nome']))
print('\033[0;31m-='*30)
print(f'\033[0;32m{len(dados["nome"])} pessoas foram cadastradas no aplicativo.\033[m')
print('\033[0;31m-='*30)
print(f'\033[0;32mMÉDIA DE IDADE: {média:.2f}\033[m')
print('\033[0;31m-='*30)
for n,i in enumerate(dados['idade']):
    if i>média:
        print('-'*30)
        print(f'\033[0;33m{dados["nome"][n]} tem a idade acima da média ({i})')
print('\033[0;31m-='*30)
print('\033[0;32mGrupo de todas as mulheres salvas no aplicativo:')
print('\033[0;31m-='*30)
for e,m in enumerate(dados['sexo']):
    if m == 'F':
        print(f'{"->":>5} {dados["nome"][e]}')