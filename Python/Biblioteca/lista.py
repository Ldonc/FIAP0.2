#Ex01
dic = {
    "oi" : "olá",
    "tchau" : "falou"
}
resp = input("Diga oi ou tchau:\n->")
print(dic[resp])


#Ex02
carros = {
    "modelo": ["celta","up","kombi","uno"],
    "portas": ["4","2","6","2"],
    "preço": [1000,200,300,100],
    "ano de fabricacao": [2014,2018,1970,2005]
}

print(carros["modelo"])
escolha = input("Qual modelo você gostaria de consultar?\n->")

for i in range(len(carros['modelo'])):
    if escolha == carros['modelo'][i]:
        indice = i
        break
for key in carros.keys():
        print(f"{key} : {carros[key][i]}")


#Ex03 e 04
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

def forca_opcao(msg,lista_opcoes):
    msg += '\n'.join(lista_opcoes) + '\n->'
    opcao = input(msg)
    while opcao not in lista_opcoes:
        print("Erro!")
        opcao = input(msg)
    return(opcao)

def acha_indice(lista,elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

carros = {
    "modelo": ["celta","up","kombi","uno"],
    "portas": ["4","2","6","2"],
    "preço": [1000,200,300,100],
    "ano de fabricacao": [2014,2018,1970,2005]
}

escolha = input("Qual modelo você gostaria de consultar?\n->")
i = local_maior(carros["preço"])
if escolha == "caro":
    i = local_maior(carros["preço"])
    print(f"O carro mais caro que temos disponível é o {carros["modelo"][i]} pelo preço de R${carros["preço"][i]}")
else:
    i = local_menor(carros["preço"])
    print(f"O carro mais caro que temos disponível é o {carros["modelo"][i]} pelo preço de R${carros["preço"][i]}")


#Ex04
local_mais_barato = local_menor(carros['preço'])
print("As infos sobre o carro mais caro são:")
for key in carros.keys():
    print(f"{key}:{carros[key][local_mais_barato]}")

#Ex05
print(carros["modelo"])
pergunta = forca_opcao("Você gostaria de cadastrar um novo carro?\n->",carros['modelo'])
if pergunta == "sim":
    qual = forca_opcao("Qual seria o modelo?\n->",carros['modelo'])
    carros["modelo"].append(qual)

#Ex06
else:
    remover = input("Você gostaria de remover algum carro?\n->")
    if remover == "sim":
        escolha = forca_opcao("Qual seria o modelo?\n->",carros['modelo'])
        ind_rem = acha_indice(carros['modelo'],escolha)
        for key in carros.keys():        
            carros[key].pop(ind_rem)
print(carros["modelo"])