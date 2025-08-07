#Ex02
nome = input("Digite seu nome:\n->")
while len(nome) < 3:
    nome = input("Digite seu nome:\n->")
while True:
    idade = input("Digite sua idade:\n->")
    if idade.isnumeric():
        idade = int(idade)
        if idade > 0 and idade < 150:
            break
        print("Só até 150!!")
    else:
        print("Tem que ser um número!")
salario = input("Digite seu salário:\n->")
while not salario.isnumeric():
    salario = input("Digite seu salário:\n->")
sexo = input("Qual seu sexo: f ou m \n->")
while sexo != "f" and sexo != "m":
    sexo = input("Qual seu sexo: f ou m \n->")
civil = input("Qual seu estado civil: s,c,v ou d")
while civil != 's' or civil != 'c' or civil != 'v' or civil != 'd':
    civil = input("Qual seu estado civil: s,c,v ou d")


#Ex03
a = 80
b = 200
t = 0
while a < b:
    a *= 1.03
    b *= 1.015
    t+=1
print(t)


#Ex06
nome = input("Cadastre seu usuário:\n->")
senha = input("Cadastre sua senha:\n->")
while nome == senha:
    print("Seu nome não pode ser igual a senha")
    nome = input("Cadastre seu usuário:\n->")
    senha = input("Cadastre sua senha:\n->")


#Ex07
i= 1 
while i < 11:
    print(f"Tabuada do {i}:\n")
    j=1
    while j < 11:
        print(f"{i}*{j} = {i*j}")
        j+= 1
        print()