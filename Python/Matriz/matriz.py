import matplotlib.pyplot as plt
from numpy.ma.core import diagonal

matriz = [[1,2,3,4] , [4,5,6,7] ,[7,8,9,10]]
plt.imshow(matriz,"hot")
plt.colorbar()
plt.show()



matriz = [[1,2,3,4] , [4,5,6,7] ,[7,8,9,10]]
print(matriz[0])
print(matriz[0][2])
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        print(matriz[i][j])


def mostra_matriz(matriz):
    for linha in matriz:
        print(linha)
    return

def cria_matriz(linhas,colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz



diagonal = cria_matriz(10,10)
for i in range(len(diagonal)):
    diagonal[i][i] = 1



xadrez = cria_matriz(8,8)
for i in range(len(xadrez)):
    for j in range(len(xadrez)):
        if i%2 == 0 :
            if j%2 == 0:
                xadrez[i][j] = 0
            else:
                xadrez[i][j] = 1
        else:
            if j % 2 == 0:
                xadrez[i][j] = 1
            else:
                xadrez[i][j] = 0




circulo = cria_matriz(1000,1000)
raio = len(circulo)/2
for i in range(len(circulo)):
    for j in range(len(circulo[0])):
        if (i-raio)**2 + (j-raio)**2 < raio ** 2:
            circulo[i][j] = i
        else:
            circulo[i][j] = 0
'''menos raio serve para centralizar o circulo'''


plt.imshow(circulo,"hot")
plt.colorbar()
plt.show()