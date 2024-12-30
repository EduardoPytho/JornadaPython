p = float(input('Digite o valor do produto: R$'))

preço = p - (p * 5 / 100)

print(f'Em uma promoção de 5% de desconto\n seu produto iria custar R${preço:.2f}')