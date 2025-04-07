def voto(an):
    from datetime import date
    atual = date.today().year
    idade = atual-an
    if idade<16:
        estado = 'NEGADO'
    elif 16 <= idade < 18:
        estado = 'OPCIONAL'
    elif 18 <= idade <= 69:
        estado = 'OBRIGATÓRIO'
    else:
        estado = 'OPCIONAL'
    return f'Com {idade} Anos: {estado}'
print('-='*20)
digitado = int(input('Qual seu ano de nascimento? '))
print('-='*20)
print(voto(digitado))
print('-='*20)