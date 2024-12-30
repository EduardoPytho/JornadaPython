silva = str(input('Insira seu nome completo e o sistema vai lhe falar se ele contém "Silva" no seu nome: ')).upper()

TF = silva.strip()

TF = TF.split()

TF = 'SILVA' in TF

print(f'Seu nome contém "Silva"? {TF}\n\nTRUE = SIM\n\nFALSE = NÃO\n')