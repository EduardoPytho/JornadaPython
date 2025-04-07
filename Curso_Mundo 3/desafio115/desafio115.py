from time import sleep
from interface import *
from arquivo import *

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)

while True:
    resposta = menu(['Cadastrar Pessoas','Listar Pessoas','Sair do Sistema'])
    if resposta == 1:
        logo('NOVO CADASTRO')
        nome = str(input('Digite o nome: ')).strip()
        idade = leiainteiro('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 2:
        lerArquivo(arq)
    elif resposta == 3:
        logo('Saindo do sistema... Até logo!')
        break
    else:
        print('\033[31mERRO! DIGITE NOVAMENTE!\033[m')
    sleep(2)