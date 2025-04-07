def maior(* valores):
    print('-='*20)
    print('Os valores informados foram os ',end='')
    for vls in valores:
        print(vls,end=' ')
    print('',end='')
    print(f'\nUm total de {len(valores)} mencionados ao todo.')
    print(f'O maior valor dos já mencionados foi o {max(valores)}')
maior(1,2,3,4,5,8)
maior(300,500,4320,324023,2400)