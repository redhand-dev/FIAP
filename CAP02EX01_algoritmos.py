print("{:^50}".format(" CONTROLE DE ASSINATURAS "))
print("")

Nome = input("Digite seu nome: ")
print("Olá,", Nome)
print("")

faturamento_anual = float(input("Por favor, informe o seu faturamento na plataforma R$ "))
print("")
print('''***CATEGORIAS***
BASIC
SILVER
GOLD
PLATINUM
''')

categoria = (input("Qual é a sua categoria atual? "))

if categoria == 'BASIC':
    print("Categoria " + categoria)
    bonus = faturamento_anual + (faturamento_anual * 30 / 100)
elif categoria == 'SILVER':
    print("Categoria " + categoria)
    bonus = faturamento_anual + (faturamento_anual * 20 / 100)
elif categoria == 'GOLD':
    print("Categoria " + categoria)
    bonus = faturamento_anual + (faturamento_anual * 10 / 100)
elif categoria == 'PLATINUM':
    print("Categoria " + categoria)
    bonus = faturamento_anual + (faturamento_anual * 5 / 100)

print("De acordo com a sua categoria " +(categoria), "e seu faturamento de R${:.2f}, o valor de bônus a receber é R${:.2f}.".format(faturamento_anual, bonus))

exit()