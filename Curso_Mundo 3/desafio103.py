def ficha(nome='<DESCONHECIDO>',gols=''):
    if nome.strip() == '':
        nome='<DESCONHECIDO>'
    if gols.isnumeric():
        int(gols)
    else:
        gols = 0
    return f'O jogador {nome} fez {gols} gol(s) no campeonato.'
print('-'*20)
user_name = str(input('Nome do jogador: ')).strip().title()
user_gols = str(input('Número de gols: '))
print('-'*20)
print(ficha(nome=user_name,gols=user_gols))