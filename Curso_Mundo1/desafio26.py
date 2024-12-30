frase = str(input('Escreva uma frase qualquer: ')).upper().strip()

contar = frase.count('A')

achar1 = frase.find('A') + 1

achar2 = frase.rfind('A') + 1

print(f'\nA frase contém {contar} "A"\n\nA posição em que foi encontrado pela primeira vez o "a" foi na posição {achar1}\n\nA posição em que foi encontrado pela última vez o "a" foi na posição {achar2}.\n\n')