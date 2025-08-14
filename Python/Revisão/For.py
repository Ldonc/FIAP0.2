for i in range (1,11):
    print(f"Tabuada do {i}: ")
    for j in range(1,11):
        print(f"{i}*{j} = {i*j}")
    print()

#Ex01
lista = [4,1,5,7,3,6,9,2,10,8]
soma = 0
media = 0
for i in range(len(lista)):
    soma += lista[i]
    media = soma / len(lista)
print(soma)
print(media)


#Ex02
lista = []
par = 0
impar = 0
for i in range(10):
    num = input("Diga um número:\n->")
    while not num.isnumeric():
        num = input("Diga um número:\n->")
    num = int(num)
    lista.append(num)
for i in range(len(lista)):
    if lista[i] % 2 == 0:
        par += 1
    else:
        impar += 1
print(f"Essa foi a quantidade de pares {par} e essa a de ímpares {impar}!!")
