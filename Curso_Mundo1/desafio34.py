salario = float(input('Digite seu salário atual:\nR$'))
if salario <1250.00:
    salario = salario+(salario*15/100)
else:
    salario = salario+(salario*10/100)
print(f'Aumento de salário feito com sucesso!\n\nSeu salário agora é de R${salario:.2f}\n')