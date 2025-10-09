import requests
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

def printa_dic(dic,num=0):
    for key in dic.keys():
        if type(dic[key]) is dict:
            print(key)
            printa_dic(dic[key],num+1)
        else:
            print(f"{num*'  '}{key} : {dic[key]}")
    return

def cadastrar():
    global indices
    for key in acougue.keys():
        if 'preço' in key.lower() or 'estoque' in key.lower():
            while True:
                try:
                    info = input(f'Diga o novo {key}: ')
                except:
                    print("Tem que ser float")
                else:
                    acougue[key].append(info)
                    break
            continue
    print(acougue)
    indices = cria_indices()
    return

def cria_indices():
    global indices
    indices = {acougue['Carnes'][i] : i for i in range(len(acougue['Carnes']))}
    return indices

def remover():
    global indices
    escolha = forca_opcao("Qual item será removido?\n",acougue['Carnes'])
    indice_escolha = indices[escolha]
    for key in acougue.keys():
        acougue[key].pop(indice_escolha)
    indice = cria_indices()
    return

def atualizar():
    item = forca_opcao("Qual item você deseja atualizar?\n->",acougue['Carnes'])
    indice_item = indices[item]
    for key in acougue.keys():
        if forca_opcao(f"Você quer atualizar {key} para {item}?\n", ['sim','não']) == 'sim':
            info = input(f"DIga o novo {key}: ")
            acougue[key][indice_item] = info
    return

def verifica_numero(msg):
    num = input(msg)
    while not num.isnumeric():
        num = input(msg)
    return int(num)


def comprar():
    item = forca_opcao("Qual item você quer comprar?", acougue['Carnes'])
    indice_item = indices[item]
    for key in acougue.keys():
        print(f"{key} : {acougue[key][indice_item]}")
    continuar = forca_opcao(f"Você quer levar {item}?",['SIM','não'])
    if continuar == 'não':
        return
    qtd = verifica_numero(f"Quantos kg de {item}?")
    if qtd <= acougue['Estoque'][indice_item]:
        acougue['Estoque'][indice_item] -= qtd
        carrinho['Valor Total'] += qtd*acougue['R$/kg'][indice_item]
        if item not in carrinho['Itens'].keys():
            carrinho['Itens'][item] = qtd
        else:
            carrinho['Itens'][item] += qtd
    else:
        print(f"Só há {acougue['Estoque'][indice_item]}kg no estoque!")
        comprar()

def cadastro_endereco():
    while True:
        cep = input("Diga seu cep: ")
        endereco = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
        if endereco.status_code == 200:
            carrinho['Endereço'] = endereco.json()
            carrinho['Endereço']['N°'] = input("Búmero da residência: ")
            carrinho['Endereço']['Complemento'] = input("Complemento")
            break
        else:
            print("CEP inválido!")
    return

def confirmar_compra():
    print('Essas são as infos da sua compra: ')
    printa_dic(carrinho)
    alterar = forca_opcao("Deseja remover algum item?",['s','n'])
    if alterar == 's':
        item = forca_opcao("Qual item vc irá remover?",carrinho['Itens'].keys())
        qtd = verifica_numero(f"Quantos kg de {item} serão removidos?")
        if qtd <= carrinho['Itens'][item]:
            carrinho['Itens'][item] -= qtd
            carrinho['Itens'][item] -= qtd*acougue['R$/kg'][indices]
        else:
            print(f"Não é possível remover esse tanto pois só há {carrinho['Itens'][item]}kg ")
        confirmar_compra()
    return

acougue = {
    'Carnes' : ['Patinho','Coxão Mole','Fraldinha','Picanha','Maminha','Linguiça'],
    'R$/kg' : [35.90,49.90,39.90,80.00,45.90,15],
    'Estoque' : [10,50,30,15,20,100],
    'Validade' : ['4','7','5','9','20','50'],
}

indices = cria_indices()

carrinho = {
    "Endereço" : {
        "Rua" : '',
        "Bairro " : '',
         "N°" : '',
         "Cep" : '',
        },
        "Itens" : {},
        "Valor Total" : 0
}

acoes = {
    'cadastrar' : cadastrar,
    'remover' : remover,
    'atualizar' : atualizar,
    'sair' : exit
}
print(cadastrar)
print("Bem-Vindo ao Açougue do Danilo 😁")
usuario = forca_opcao("Você é",['cliente','funcionário'])
if usuario == 'cliente':
    cadastro_endereco()
while True:
    if usuario == 'funcionário':
        operacao = forca_opcao("Qual operação será realizada?",['cadastrar','remover','atualizar'])
        acoes[operacao]()
    else:
        comprar()
        encerrar = forca_opcao("Encerrar a compra ou ver mais itens?",['encerrar','continuar'])
        if encerrar == 'encerrar':
            print(f"Você vai levar\n{list(carrinho['Itens'].keys())[0]} em {carrinho['Endereço']['logradouro']}")
            print(carrinho)
            break