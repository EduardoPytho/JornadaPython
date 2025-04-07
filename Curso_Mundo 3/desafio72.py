lista = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')
Número = int(input('Escreva um número de 1 a 20: '))
if Número >20 or Número <0:
    while True:
        Número = int(input('Número inválido, Por favor, insira um número de 1 a 20: '))
        if Número <21 and Número >-1:
            break
print(f'Você digitou o número {lista[Número].lower()}.')