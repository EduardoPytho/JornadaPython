from random import randint
from time import sleep
from operator import itemgetter
jogadores = {'Jogador 1':randint(1,6),'Jogador 2':randint(1,6),'Jogador 3':randint(1,6),'Jogador 4':randint(1,6)}
ranking = dict()
for J,dado in jogadores.items():
    print(f'{J} jogou o dado, e o número foi {dado}')
    sleep(0.9)
print('-'*50)
print('Ranking dos jogadores:')
ranking = sorted(jogadores.items(),key=itemgetter(1),reverse=True)
for i,v in enumerate(ranking):
    print(f'{i+1}° Lugar = {v[0]} com {v[1]}.')
    sleep(1)