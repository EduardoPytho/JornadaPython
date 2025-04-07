from time import sleep
dados_permanente = list()
dados = dict()
esc = ''
while esc != 'N':
    dados.clear()
    print('=-'*30)
    dados['Nome'] = str(input('Nome do Jogador: ')).strip().title()
    dados['Partidas GOLS'] = list()
    dados['total de gols'] = 0
    partidas_jogadas = int(input(f'Quantas partidas o {dados["Nome"]} jogou? '))
    for r in range(1, partidas_jogadas + 1):
        gols = int(input(f'Quantos gols {dados["Nome"]} fez na partida {r}? '))
        dados['Partidas GOLS'].append(gols)
        dados['total de gols'] += gols
    dados_permanente.append(dados.copy())
    esc = str(input('Inserir outro jogador? [S/N] ')).strip().upper()[0]
print('-='*60)
print(dados)
print('-='*60)
sleep(0.5)
print(f'Código      -      Jogador      -      total')
for k, v in enumerate(dados_permanente):
    print(f'{k:<6}      -      {v["Nome"]:>6}   -      {v["total de gols"]:^4}')
while True:
    print('=-'*30)
    escolha = int(input('Deseja ver informações de qual jogador? escreva o código (999 para encerrar.): '))
    if escolha >= len(dados_permanente) and escolha > 999 or escolha <999:
        while True:
            print('Erro! código inválido.')
            escolha = int(input('Deseja ver informações de qual jogador? escreva o código (999 para encerrar.): '))
            if escolha < len(dados_permanente):
                break
    elif escolha == 999:
        break
    print(f'Nome:{dados_permanente[escolha]["Nome"]}\nO jogador jogou {len(dados_permanente[escolha]["Partidas GOLS"])}')
    for n,g in enumerate(dados_permanente[escolha]["Partidas GOLS"]):
        print(f'{"->":>4}Na partida {n}, fez {g} gols.')
    print(f'Somando um total de {dados_permanente[escolha]["total de gols"]} gols em todas as partidas.')
print('<< VOLTE SEMPRE! >>')