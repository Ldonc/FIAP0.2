ini = 0
fim = 25
num = 25

while True:
    chute = (ini + fim )/ 2
    if chute**2 > num:
        fim = chute
    else:
        ini = chute
    if abs(chute**2 - num) < 0.01:
        break
    print(chute)


def busca_binaria(num):
    ini = 0
    fim = num 
    chute = (ini+fim)/2
    while fim - ini > 0.001:
        if  chute**2 > num:
            fim = chute 
        else:
            ini = chute 
        print(chute)
    return chute 

busca_binaria(25)