from datetime import datetime
informações = dict()
ano_atual = datetime.today().year
informações['Nome'] = str(input('Nome: ')).strip().capitalize()
informações['idade'] = ano_atual-int(input('Ano de nascimento: '))
informações['Carteira de Trabalho'] = int(input('Número da Carteira de Trabalho (0 se não tiver): '))
if informações['Carteira de Trabalho'] != 0:
    informações['Ano de Contratação'] = int(input('Ano de contratação: '))
    informações['Salário'] = int(input('Salário: '))
    informações['Aposentadoria'] = informações['idade']+((informações['Ano de Contratação'] + 35)-ano_atual)
print('\n')
for c,i in informações.items():
    print(f'O {c} é igual a {i}')