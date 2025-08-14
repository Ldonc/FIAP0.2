def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    num = int(num)
    return num

def forca_opcao(msg,lista_opcoes):
    escolha = input(msg)
    while escolha not in lista_opcoes:
        escolha = input(msg)
    return escolha

def calcula_media(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    media = soma / len(lista)
    return media

def local_maior(lista):
    indice_maior = 0
    maior = lista[indice_maior]
    for i in range(len(lista)):
        if lista[i] > maior:
            indice_maior = i
            maior = lista[indice_maior]
    return indice_maior

def local_menor(lista):
    indice_menor = 0
    menor = lista[indice_menor]
    for i in range(len(lista)):
        if lista[i] < menor:
            indice_menor = i
            menor = lista[indice_menor]
    return indice_menor



print("Seja Bem Vindo")
rua = input("Onde você mora?\n->")
ano = verifica_numero("Em que ano você nasceu?\n->")
if ano > 2007:
    print("Você não pode beber 😘👌!!!")
else:
    lista_vinhos = ["vinho tinto", "vinho rose", "vinho branco", "vinho seco"]
    lista_precos = [95,80,75,90]
    valor_medio = calcula_media(lista_precos)
    print(f"Este é o valor médio de nossos vinhos {valor_medio}R$")

    preco_maior = local_maior(lista_precos)
    print(f"Este é o valor do nosso vinho mais caro {lista_precos[preco_maior]}R$")

    preco_menor = local_menor(lista_precos)
    print(f"Este é o valor do nosso vinho mais barato {lista_precos[preco_menor]}R$")
    
    print(lista_vinhos)
    vinho_escolhido = forca_opcao("Qual vinho você gostaria?\n->",lista_vinhos)
    
    garrafas = verifica_numero("De quantas garrafas você gostaria?\n->")