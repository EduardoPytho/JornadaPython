from time import sleep
def contador(inicio,fim,passo):
    print('=-'*20)
    sleep(0.5)
    if passo == 0 and inicio>fim:
        passo = -1
    elif passo == 0 and inicio<fim:
        passo = 1
    print(f'Contagem de {inicio} até {fim} pulando por {passo}:')
    if inicio>fim and passo >0:
        passo = -passo
    ajuste_fim = 1 if passo>0 else -1
    for cont in range(inicio,fim+ajuste_fim,passo):
        print(cont,end=' ',flush=True)
        sleep(0.5)
    print('FIM!')
    print('')
contador(1,10,1)
contador(10,0,2)
print('=-'*20)
início = int(input('Vamos fazer uma personalizada!\nEm qual número iremos começar? '))
final = int(input('Até? '))
Passo_a_passo = int(input('indo de quanto a quanto? '))
print('Ok!\n\033[1;35mprocessando..\033[m')
sleep(1)
contador(início,final,Passo_a_passo)