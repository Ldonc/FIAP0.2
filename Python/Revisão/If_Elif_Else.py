#Ex 01
num1 = int(input("Escreva um número:\n->"))
num2 = int(input("Escreva outro número:\n->"))

if num1 > num2 :
    print(f"Esse é o seu maior número {num1}")
else:
    print(f"Esse é o seu maior número {num2}")


#Ex 02
ano = int(input("Em que ano você nasceu?\n->"))

if ano > 2007 :
    print("Você não poderá votar esse ano!!!")
else:
    print("Você poderá votar esse ano!!!")


#Ex03
senha = "1234"
digite = input("Digite a senha para acessar:\n->")

if digite == senha:
    print("ACESSO PERMITIDO!!!")
else:
    print("ACESSO NEGADO!!!")


#Ex04
macas = int(input("De quantas maçãs você gostaria?\n->"))

if macas >= 12 :
    print(f"O valor da sua compra foi de {macas*0.25}")
else:
    print(f"O valor da sua compra foi de {macas*0.3}")


#Ex06
sexo = input("Você é homi ou mulier?\n->mulier = 1\n->homi = 2\n\n->")
altura =  float(input("Qual a sua altura?\n->"))
if sexo == "1":
    print(f"Seu peso ideal é de {(62.1*altura)-44.7}")
else:
    print(f"Seu peso ideal é de {(72.7 * altura) - 58}")


#Ex07
lados = int(input("Digite o número de lados que seu poligono regular possuí:\n->"))
mede = float(input("Digite a medida dos lados:\n->"))

if lados == 3:
    print("Seu poligono é um triângulo")
elif lados == 4:
    print("Seu poligono é um quadrado")
elif lados == 5:
    print("Seu poligono é um pentágono")
print(f"E seu perímetro mede {mede*lados}cm")


#Ex08
lados = int(input("Digite o número de lados que seu poligono regular possuí:\n->"))
if lados < 3:
    print("ISSO NÂO È UM POLIGONOOOO")
elif lados > 5:
    print("POLIGONO NÃO IDENTIFICADO")
else:
    mede = float(input("Digite a medida dos lados:\n->"))

    if lados == 3:
        print("Seu poligono é um triângulo")
    elif lados == 4:
        print("Seu poligono é um quadrado")
    else:
        print("Seu poligono é um pentágono")
    print(f"E seu perímetro mede {mede*lados}cm")


#Ex09
a = int(input("Digite um número:\n->"))
b = int(input("Digite um número:\n->"))
c = int(input("Digite um número:\n->"))

if a>b and a>c:
    print(a)
elif b>c:
    print(b)
else:
    print(c)

#Outra forma de resolver
a = int(input("Digite um número:\n->"))
b = int(input("Digite um número:\n->"))
c = int(input("Digite um número:\n->"))

maior = a
if b>maior:
    maior = b
if c > maior:
    maior = c


#Ex05
a = int(input("Digite um número:\n->"))
b = int(input("Digite um número:\n->"))
c = int(input("Digite um número:\n->"))

if a>b and a>c:
    aux = a
    a = c
    c = aux
elif b>c:
    aux = b
    b = c
    c = aux
if a>b:
    aux = a
    a = b
    b = aux
print(a,b,c)