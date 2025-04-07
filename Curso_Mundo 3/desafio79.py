valores = []

while True:
    digitado = int(input('\033[0;36mDigite o valor: \033[0;33m'))
    if digitado in valores:
        print('\033[1;31mValor já incluído na lista..')
    elif digitado not in valores:
        valores.append(digitado)
        print('\033[1;35m=-'*40)
        print('\033[1;32mValor inserido com sucesso na lista!')
    print('\033[1;35m=-'*40)
    esc = str(input('\033[mDeseja continuar inserindo valores? (\033[1;32mS\033[m/\033[1;31mN\033[m): \033[0;33m')).upper().strip()
    print('\033[1;35m=-'*40)
    if esc == 'N':
        print('\033[m')
        break
    if esc != 'S' and esc != 'N':
        print('\033[1;31mEscolha inválido.\033[m')
print(f'\nVocê salvou na lista os seguintes valores: {sorted(valores)}.')