dal = int(input('Quantos dias alugados? '))
kms = float(input('Quantos KM rondados? '))
dalc = dal*60                                 #cada dia = R$60#
kmsc = (kms*0.15)                             #cada km = R$0,15#
kmsdalt = dalc+kmsc
print(f'Total a pagar R${kmsdalt:.2f}')