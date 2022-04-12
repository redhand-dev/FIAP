total = [0,0,0]
dia_semana =['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira', 'Quinta-Feira', 'Sexta-Feira']

print(' 2 - Segunda-Feira \n 3 - Terça-Feira \n 4 - Quarta-Feira \n 5 - Quinta-Feira \n 6 - Sexta-Feira \n')
voto = int(input('Escolha até dois dias da semana para a Live\nEncerre a sua votação digitando -1 \nDigite o número correspondente: '))
while voto != -1:
    total[voto-1] += 1                           
    print(' 2 - Segunda-Feira \n 3 - Terça-Feira \n 4 - Quarta-Feira \n 5 - Quinta-Feira \n 6 - Sexta-Feira \n')
    voto = int(input('Escolha até dois dias da semana para a Live:\nEncerre a sua votação digitando -1 \nDigite o número correspondente: '))

totalvotos = sum(total)                            
vencedor = max(total)                               

for i in range(len(total)):
    perc = total[i]/totalvotos * 100
    print('\nDia da semana: {0}\nVotos recebidos: {1}\nPercentual:{2:.2f}%'.format(dia_semana[i],total[i], perc))
    if vencedor == total[i]:
        v = i

print('\n\n', dia_semana[v], 'foi o dia escolhido para a Live!')