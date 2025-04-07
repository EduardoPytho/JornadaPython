p = '.'
real = 'R$'
k = 0
print('-='*20,'TABELA OFICINA GAMER','-='*20,'\n')
lista = ('intel i5 13420H',300.99,'RTX 4060 6gb VRAM',3400.99,'GTX 1660 8gb VRAM',1200.99,'16gb RAM 3550 Mhz',900.99,'PC Acer Aspire 5',3500.99)
for t in range(0,len(lista),2):
    print(f'{lista[t]:^20}{p:.^20}  {real:>}{lista[t+1]:>10}\n')
print('-='*52)