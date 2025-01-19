soma = 0
mih = 0
mihn = ''
mul20 = 0
for ks in range(1,5):
    print(f'===== {ks}° Pessoa =====')
    Nome = str(input('Nome:'))
    idade = int(input('Idade:'))
    sexo = int(input('Sexo: \n1 - Masculino\n2 - Feminino\n\nDigite:'))
    soma = idade+soma
    if ks == 1 and sexo == 1:
        mih = idade
        mihn = Nome
    if sexo == 1 and ks>1 and idade>mih:
        mih = idade
        mihn = Nome
    if sexo == 2 and idade <20:
        mul20 += 1
média = soma/4
print(f'A média de idade das 4 pessoas são \033[1;33m{média}\033[m')
if mih >= 1:
    print(f'O homem mais velho das 4 pessoas é o \033[1;33m{mihn}\033[m')
elif mih == 0:
    print('Não existe nenhum homem nesse grupo.')
if mul20 == 1:
    print(f'\033[1;33m{mul20}\033[m Mulher nesse grupo tem menos de 20 anos.')
elif mul20 >1:
    print(f'\033[1;33m{mul20}\033[m Mulheres nesse grupo tem menos de 20 anos.')
elif mih == 0:
    print('Não existe nenhuma mulher com menos de 20 anos nesse grupo.')