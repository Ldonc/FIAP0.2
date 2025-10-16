def indice_menor(lista):
    indice = 0
    for i in range(len(lista)):
        if lista[i] < lista[indice]:
            indice = i
    return indice

original = [3,1,5,6,2,4,7]
nova = []
for i in range(len(original)):
    menor_indice = indice_menor(original)
    nova.append(original[menor_indice])
    original.pop(menor_indice)
    print(original)
    print(nova)


def selection_sort(lista):
    ordenada = []
    while lista:
        local_menor = indice_menor(lista)
        menor = lista.pop(local_menor)
        ordenada.append(menor)
        print(lista)
        print(ordenada)
        print()
    return ordenada

lista = [3,1,5,6,2,4,7]
ordenada = selection_sort(lista)



lista = [3, 1, 5, 6, 2, 4, 7]
for i in range(len(lista)):
    menor_indice = indice_menor(lista[:len(lista)-i])
    a = lista.pop(menor_indice)
    lista.append(a)
    print(lista)



lista = [3, 1, 5, 6, 2, 4, 7]
for i in range(len(lista)):
    local_menor = indice_menor(lista[i:]) + i
    aux = lista[i]
    lista[i] = lista[local_menor]
    lista[local_menor] = aux
    print(lista)