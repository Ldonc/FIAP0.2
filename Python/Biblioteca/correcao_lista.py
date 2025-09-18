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

atualizar = forca_opcao("Qual carro você deseja atualizar?",carros['modelo'])
indice_atualizar = acha_indice(carros['nome'],atualizar)
for key in carros.keys():
    carros[key][indice_atualizar] = input(f"Diga o novo {key} do {atualizar}")


#Ex07
frase = "O bispo de Constantinopla é um bom desconstantinopolitanizador. Quem o desconstantinopolitanizar, um bom desconstantinopolitanizador será."
frase = frase.lower()
for char in ',.:;?!':
    frase = frase.replace(char,"")
print(frase)
palavras = frase.split(' ')
contador = {}
for palavra in palavras:
    if palavra not in contador.keys():
        contador[palavras] = 1
    else:
        contador[palavras] += 1


#Ex08
numeros ={
    'zero' : '0',
    'três' : '3',
    'nove' : '9',

}
frase = "Eu tenho aula na sala nove zero três"
for key in numeros.keys():
    frase = frase.replace(key+' ', numeros[key])
    frase = frase.replace(key,numeros[key])
print(frase)


#Ex09
dic_1 = {
    'a' : 10,
    'b' : 20,
    'd' : 30,
}
dic_2 = {
    'b' : 10,
    'c' : 20,
    'd' : 30,
}

interseccao_chaves = []
for key_1 in dic_1.keys():
    if key_1 in dic_2.keys():
        interseccao_chaves.append(key_1)
print(interseccao_chaves)


#Ex10
disjuncao = []
for key_1 in dic_1.keys():
    if key_1 not in dic_2.keys():
        disjuncao.append(key_1)

for key_2 in dic_2.keys():
    if key_2 not in dic_1.keys():
        disjuncao.append(key_2)
print(disjuncao)
