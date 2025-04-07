from time import sleep
def notas(*notes,sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param notes: Recebe as notas dos alunos.
    :param sit: se True, retorna junto com os dicionários, a situação da média dos alunos.
    :return: Retorna um dicionário com as seguintes coisas: Contagem de notas,Nota máxima,Nota mínima e a Média dos alunos.
    """
    somas = 0
    for num in notes:
        somas+=num
    lista = {'Contagem de Notas':len(notes), 'Máximo':max(notes), 'Mínimo':min(notes), 'Média': somas / len(notes)}
    if sit:
        if lista['Média'] <= 4.9:
            lista['Estado'] = 'PÉSSIMO'
        elif 5.0 >= lista['Média'] <= 6.9:
            lista['Estado'] = 'Ruim'
        elif 7.0 >= lista['Média'] <= 7.9:
            lista['Estado'] = 'Regular'
        elif 8.0 >= lista['Média'] <= 8.9:
            lista['Estado'] = 'Aceitável'
        elif 9.0 >= lista['Média'] <= 9.9:
            lista['Estado'] = 'Ótimo'
        elif lista['Média'] == 10.0:
            lista['Estado'] = 'Excelente!'
    return lista
sleep(2)
print(notas(9.6,4.3,10,8.3))
print('-='*30)
sleep(2)
print(notas(10.0,8.7,9.5,7.0,9.8,sit=True))
print('-='*30)
sleep(2)
print(help(notas))
print('-='*30)