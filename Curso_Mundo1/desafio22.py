NomeComp = str(input('Insira seu nome completo: '))

NomeMAIS = NomeComp.upper()

NomeMINU = NomeComp.lower()

NomeSEES = NomeComp.strip()

NomeSEES = NomeSEES.replace(' ','')

NOMENL = (NomeComp.split())

NOMENL = len(NOMENL [0])

print(f'Maiúsculas totalmente: {NomeMAIS}\nMinúsculas totalmente: {NomeMINU}\nSem espaços: {NomeSEES}\nContagem de letras do primeiro nome: {NOMENL}')