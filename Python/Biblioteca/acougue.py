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

def cadastrar():
    for key in acougue.keys():
        info = input(f"Diga o novo {key}:\n->")
        acougue[key].append(info)
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
        indice = cria_indices()
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

print("Bem-Vindo ao Açougue do Danilo 😁")
usuario = forca_opcao("Você é",['cliente','funcionário'])

while True:
    if usuario == 'funcionário':
        operacao = forca_opcao("Qual operação será realizada?",['cadastrar','remover','atualizar'])
        if operacao == 'cadastrar':
            cadastrar()
        elif operacao == 'remover':
            remover()
        else:
            atualizar()
        continuar = forca_opcao("Você deseja realizar outra operação?",['sim','não'])
        if continuar == 'não':
            break
    else:
        comprar()
        encerrar = forca_opcao("Encerrar a compra ou ver mais itens?",['encerrar','continuar'])
        if encerrar == 'encerrar':
            print(f"Você vai levar\n{list(carrinho['Itens'].keys())[0]} em {carrinho['Endereço']['logradouro']}")
            print(carrinho)
            break