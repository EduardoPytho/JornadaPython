from random import choice
a = str(input('Nome do primeiro aluno: '))
aa = str(input('Nome do segundo aluno: '))
aaa = str(input('Nome do terceiro: '))
aaaa = str(input('Nome do quarto aluno: '))
alunos = [a,aa,aaa,aaaa]
andom = choice(alunos)
print(f'O aluno escolhido foi......{andom}!')
