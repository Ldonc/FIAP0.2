#Ex01
matriz = [[0,0,0],[0,0,0],[0,0,0]]
def mostra_matriz(matriz):
    for linha in range(len(matriz)):
        print(matriz[linha])
    return

mostra_matriz(matriz)


#Ex02
matriz = []
def cria_matriz(linha,coluna):
    for i in range(linha):
        linhas = []
        for j in range(coluna):
            linhas.append(0)
        matriz.append(linhas)
    return matriz

print(cria_matriz(5,5))

#Ex03
def mostra_matriz(matriz):
    for linha in range(len(matriz)):
        print(matriz[linha])
    return

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matriz)):
    matriz[i][i] = 1
mostra_matriz(matriz)

#Ex04
def mostra_matriz(matriz):
    for linha in range(len(matriz)):
        print(matriz[linha])
    return

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(matriz)):
    j = len(matriz) -i -1
    matriz [i][j] = 1
mostra_matriz(matriz)

#Ex05
def mostra_matriz(matriz):
    for linha in range(len(matriz)):
        print(matriz[linha])
    return

def cria_matriz(linha,coluna):
    matriz = []
    for i in range(linha):
        linhas = []
        for j in range(coluna):
            linhas.append(0)
        matriz.append(linhas)
    return matriz

def jMenorI(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j<i:
                matriz[i][j] = 1
    return matriz

matriz = cria_matriz(3,3)
mostra_matriz(jMenorI(matriz))

def jMaiorI(matriz):
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if j>i:
                matriz[i][j] = 1
    return matriz

mostra_matriz(jMaiorI(matriz))

#Ex06
def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def mostra_matriz(matriz):
    for linha in range(len(matriz)):
        print(matriz[linha])
    return

def transposta(matriz):
    for i in range(len(matriz)):
        for j in range(i):
            aux = matriz[i][j]
            matriz[i][j] = matriz[j][i]
            matriz[j][i] = aux
    return matriz

matriz = [[1,2,3],[4,5,6],[7,8,9]]
mostra_matriz(transposta(matriz))