dic = {"chave" : "valor"}
print(dic["chave"])
dic["nova chave"] = "novo valor"
print(dic)
dic["chave"] = "123"
print(dic)

import random
saudacoes = {
    "oi":["Olá","Salve","Iae","BÃO uai"],
    "tchau":["Flw","tchau migo","bjsss diva","até mais"]
}
while True:
    resposta = input("Diga oi ou tchau:\n->")
    print(random.choice(saudacoes[resposta]))



qtd = {
    "3":"triangulo",
    "4":"quadrado",
    "5":"pentagono",
    "6":"hexagono"
}
lados = input("Quantos lados tem seu poligono de 3 à 6:\n->")
while lados not in qtd:
    lados = input("Quantos lados tem seu poligono de 3 à 6:\n->")
else:
    print(f"De acordo com a quantidade de lados infomada seu poligono é um {qtd[lados]}")



emojis = {
    ":)":"😊",
    ":(":"😞",
    "S2":"❤️",
    ";)":"😉"
}
texto = "Eu AMO python S2"
for key in emojis.keys():
    texto = texto.replace(key,emojis[key])
print(texto)



num = {
    "um" : "1",
    "dois" : "2",
    "tres" : "3",
    "quatro" : "4",
    "cinco" : "5",
    "seis" : "6",
    "sete" : "7",
    "oito" : "8",
    "nove" : "9"
}

telefone = input("Qual o número do seu telefone?\n->")
for key in num.keys():
    telefone = telefone.replace(key,num[key])
    telefone = telefone.replace(' ','')
print(telefone)



dic = {
    "nome" : ["danilo","lucas","matheus"],
    "idade" : [28,18,22]
}
for i in range(len(dic["nome"])):
    for key in dic.keys():
        print(f"{key} : {dic[key][i]}")
    print()



frase = "A aranha arranha a rã. A rã arranha a aranha. Nem a aranha arranha a rã. Nem a rã arranha a aranha."
print(frase)
frase = frase.lower()
print(frase)
frase = frase.replace(".","")
print(frase)
palavras = frase.split(" ")
print(palavras)

contador = {}
for i in range(len(palavras)):
    if palavras[i] not in contador.keys():
        contador[palavras[i]] = 1
    else:
        contador[palavras[i]] += 1
    print(contador)
