salario = float(input('==REALIZADOR DE AUMENTO DE SALÁRIO==\n\n\nQual seu salário atual ?\n R$'))

salarionov = salario + (salario*15/100)

print(f'Seu aumento foi realizado com sucesso!\n\nAntigo: R${salario:.2f}\n\nNovo: R${salarionov:.2f}\n')