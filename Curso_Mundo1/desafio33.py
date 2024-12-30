n1 = int(input('número 1: '))
n2 = int(input('número 2: '))
n3 = int(input('número 3: '))
maior = n2
menor = n1
if n1>n2 and n1>n3:
 maior = n1 
elif n3>n1 and n3>n2:
 maior = n3
elif n2<n1 and n2<n3:
 menor = n2
elif n3<n1 and n3<n2:
 menor = n3
print(f'\n\nMaior número = {maior}\n\nMenor = {menor}\n\n')