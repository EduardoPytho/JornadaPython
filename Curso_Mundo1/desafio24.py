santo = str(input('Digite o nome de sua cidade e eu irei falar se ele começa ou não com Santo: ')).upper()

trfl1 = santo.split()

trfl2 = 'SANTO' in trfl1[0]

print(f'Sua cidade começa com o nome Santo?\nA resposta é {trfl2}\ntrue = Sim\nfalse = Não')