distância = int(input('Qual a distância já percorrida? (em KM) '))
if distância <=200:
 distância = float(distância*0.15)
else:
 distância = float(distância*0.45)
print(f'O custo da viagem irá ser R${distância:.2f}')
