logo = 'Brasileirão 2025'
tabela = ('Botafogo','Palmeiras','Flamengo','Fortaleza','Internacional','São Paulo','Corinthians','Bahia','Cruzeiro','Vasco da Gama','EC Vitória','Atlético-MG','Fluminense','Grêmio','Juventude','Bragantino','Athletico-PR','Criciúma','Atlético-GO','Cuiabá')
print('-'*30)
print(f'{logo:^30}')
print('-'*30)
print(f'Primeiros colocados: {tabela[0:5]}\n')
print(f'Últimos colocados: {tabela[-4:]}\n')
print(f'Os colocados em ordem alfabética: {sorted(tabela)}\n')
print(f'A posição do Grêmio é {tabela.index("Grêmio")+1}° Lugar')