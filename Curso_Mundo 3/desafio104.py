def leiaint(pergunta='insira um num '):
    pergunta = input(pergunta)
    if pergunta.strip() == '' or not pergunta.isdigit():
        while not pergunta.isdigit():
            print('-'*30)
            pergunta = input('\033[1;31mERRO! Insira um número válido: ')
            print('\033[m',end='')
        int(pergunta)
        return pergunta
    else:
        int(pergunta)
        return pergunta

num = leiaint('Insira um número: ')
print('-'*30)
print(f'Você acabou de digitar o número {num}.')
print('-'*30)