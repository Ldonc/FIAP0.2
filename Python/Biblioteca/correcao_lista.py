def forca_opcao(msg,lista_opcoes):
    msg += '\n'.join(lista_opcoes) + '\n->'
    opcao = input(msg)
    while opcao not in lista_opcoes:
        print("Erro!")
        opcao = input(msg)
    return(opcao)


#Ex01
dic = {
    'oi' : 'olá',
    'tchau' : 'flw',
}

resposta = input("Diga oi ou tchau: ")
print(dic[resposta])


def acha_indice(lista,elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

def indice_maior(lista):
    indice_maior = 0
    for i in range(len(lista)):
        if lista[i] > lista[indice_maior]:
            indice_maior = i
    return indice_maior

def indice_menor(lista):
    indice_menor = 0
    for i in range(len(lista)):
        if lista[i] < lista[indice_menor]:
            indice_menor = i
    return indice_menor


#Ex02
carros = {
    "modelo": ["celta","up","kombi","uno"],
    "portas": ["4","2","6","2"],
    "preço": [1000,200,300,100],
    "ano de fabricacao": [2014,2018,1970,2005]
}

escolha = forca_opcao("Qual carro você quer?",carros["modelo"])
indice_escolha = acha_indice(carros['modelo'],escolha)
for key in carros.keys():
    print(f"{key} : {carros[key][indice_escolha]}")

#Ex03
local_mais_caro = indice_maior(carros['preço'])
print("As infos sobre o carro mais caro são:")
for key in carros.keys():
    print(f"{key}:{carros[key][local_mais_caro]}")

#Ex04
local_mais_barato = indice_menor(carros['preço'])
print("As infos sobre o carro mais caro são:")
for key in carros.keys():
    print(f"{key}:{carros[key][local_mais_barato]}")

#Ex05
for key in carros.keys():
    info = input(f"Diga o novo {key}: ")
    carros[key].append(info)
print(carros)

#Ex06
remover = forca_opcao("Qual carro você quer remover?",carros['modelo'])
indice_remover = acha_indice(carros['nome'],remover)
for key in carros.keys():
    carros[key].pop(indice_remover)
print(carros)