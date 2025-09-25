def forca_opcao(msg,lista_opcoes):
    msg += '\n'.join(lista_opcoes) + '\n->'
    opcao = input(f"{msg}")
    while opcao not in lista_opcoes:
        print("Inválido!")
        opcao = input(f"{msg}")
    return opcao

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

def cadastrar():
    for key in acougue.keys():
        info = input(f"Diga o novo {key}:\n->")
        acougue[key].append(info)
    return

def cria_indices():
    indices = {acougue['Carnes'][i] : i for i in range(len(acougue['Carnes']))}
    return indices

def remover():
    escolha = forca_opcao("Qual item será removido?\n",acougue['Carnes'])
    indice_escolha = indices[escolha]
    for key in acougue.keys():
        acougue[key].pop(indice_escolha)
    return

def atualizar():
    item = forca_opcao("Qual item você deseja atualizar?\n->",acougue['Carnes'])
    indice_item = indices[item]
    for key in acougue.keys():
        if forca_opcao(f"Você quer atualizar {key} para {item}?\n", ['sim','não']) == 'sim':
            info = input(f"DIga o novo {key}: ")
            acougue[key][indice_item] = info
        return



acougue = {
    'Carnes' : ['Patinho','Coxão Mole','Fraldinha','Picanha','Maminha','Linguiça'],
    'R$/kg' : [35.90,49.90,39.90,80.00,45.90,15],
    'Estoque' : [10,50,30,15,20,100],
    'Validade' : ['4','7','5','9','20','50'],
}

indices = cria_indices()

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
elif acao == '2':
    cadastrar()
    indice = cria_indices()
elif acao == '3':
    remover()
    indice = cria_indices()
elif acao == '4':
    atualizar()
else:
    print()