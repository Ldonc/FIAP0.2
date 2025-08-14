def calcula_media(lista):
    soma = 0
    for i in range(len(lista)):
        soma += lista[i]
    media = soma / len(lista)
    return media

lista = [4,1,5,7,3,6,9,2,10,8]
media = calcula_media(lista)
print(media)

lista_2 = [4,1,5,7,10,8]
media = calcula_media(lista_2)
print(media)


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

carros = ["up","fox","gol","polo","fusca"]
s_ou_n = ["sim","não"]
carro = forca_opcao("Qual carro voce quer?\n->",carros)
continuar = forca_opcao("Você quer continuar?\n->",s_ou_n)