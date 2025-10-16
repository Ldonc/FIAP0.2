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