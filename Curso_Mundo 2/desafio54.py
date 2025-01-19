from datetime import date
anoat = date.today().year
mi = 0
mei = 0
for datas in range(0,7):
    ano = int(input('Escreva seu ano de nascimento: \033[0;33m'))
    idade = anoat - ano
    if idade >= 18:
        mi += 1
    else:
        mei += 1
print(f'Entre as 7 pessoas, {mi} atingiram maior idade e {mei} ainda não estão na maior idade.')