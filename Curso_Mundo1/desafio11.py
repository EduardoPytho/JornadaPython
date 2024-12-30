lg = float(input('Digite a largura da parede (em metros) : '))

alt = float(input('Digite a altura da parede (em metros) : '))

área = lg * alt

t = área / 2
print(f'A dimensão da parede é de {lg}x{alt}, e sua área é de {área}m²')

print(f' (Supondo que em cada balde de tinta tem 1 litro, e pinta 2m²)\n Você irá precisar de {t}L de tinta.')