aluno = dict()
aluno['Nome'] = str(input('Nome: '))
aluno['Média'] = float(input(f'Média do {aluno["Nome"]}: '))
if aluno['Média'] >= 7.5:
    aluno['Estado'] = 'Passou de ano por média'
elif aluno['Média'] <7.5 and aluno['Média'] >= 5.0:
    aluno['Estado'] = 'Recuperação'
elif aluno['Média'] <5.0:
    aluno['Estado'] = 'Reprovado'
for n,i in aluno.items():
    print(f'O \033[0;32m{n}\033[m é igual a \033[0;31m{i}\033[m')