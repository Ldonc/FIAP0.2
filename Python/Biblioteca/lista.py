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