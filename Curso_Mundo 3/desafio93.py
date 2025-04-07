from time import sleep
dados = dict()
dados['Nome'] = str(input('Nome do Jogador: ')).strip().capitalize()
dados['Partidas GOLS'] = list()
dados['total de gols'] = 0
partidas_jogadas = int(input(f'Quantas partidas o {dados["Nome"]} jogou? '))
for r in range(1,partidas_jogadas+1):
    gols = int(input(f'Quantos gols {dados["Nome"]} fez na partida {r}? '))
    dados['Partidas GOLS'].append(gols)
    dados['total de gols'] += gols
print('-='*60)
print(dados)
print('-='*60)
sleep(0.5)
for k,i in dados.items():
    print(f'O dado {k} tem o valor {i}')
sleep(0.5)
print('-='*60)
print(f'O jogador {dados["Nome"]} jogou {partidas_jogadas} partidas.')
sleep(0.5)
for c,g in enumerate(dados['Partidas GOLS']):
    print(f'{"=> ":>9}Na partida {c+1}, O jogador fez {g} gols.')
