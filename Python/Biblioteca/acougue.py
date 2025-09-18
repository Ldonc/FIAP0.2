def forca_opcao(msg,lista_opcoes):
    msg += '\n'.join(lista_opcoes) + '\n->'
    opcao = input(msg)
    while opcao not in lista_opcoes:
        print("Erro!")
        opcao = input(msg)
    return(opcao)

def acha_indice(lista,elem):
    for i in range(len(lista)):
        if lista[i] == elem:
            return i

def indice_maior(lista):
    indice_maior = 0
    for i in range(len(lista)):
        if lista[i] > lista[indice_maior]:
            indice_maior = i
    return indice_maior

def indice_menor(lista):
    indice_menor = 0
    for i in range(len(lista)):
        if lista[i] < lista[indice_menor]:
            indice_menor = i
    return indice_menor

def info_carne(dic):
    escolha = forca_opcao("Qual carne você quer?", acougue["Carnes"])
    indice_escolha = acha_indice(acougue['Carnes'], escolha)
    for key in acougue.keys():
        print(f"{key} : {acougue[key][indice_escolha]}")
    return info_carne


acougue = {
    'Carnes' : ['Patinho','Coxão Mole','Fraldinha','Picanha','Maminha','Linguiça'],
    'R$/kg' : [35.90,49.90,39.90,80.00,45.90,15],
    'Estoque' : [10,50,30,15,20,100],
    'Validade' : ['4','7','5','9','20','50'],
}

menu = '''
Bem-Vindo ao Açougue do Danilo 😁

    1.Informações
    2.Cadastrar
    3.Remover
    4.Atualizar
    5.Escolher
'''
print(menu)
acao = input("O que você deseja fazer?\n->")
if acao == '1':
    info_carne(acougue)
if acao == '2':
    print()