def logo(msg):
    print('~' * (len(msg) + 2))
    print(f' {msg} ')
    print('~' * (len(msg) + 2))
mensagem = str(input('digite: '))
logo(mensagem)