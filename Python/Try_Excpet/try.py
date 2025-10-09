while True:
    try:
        a = int(input("Digite um número\n-> "))
        break
    except:
        print("Valor inválido!!!")


while True:
    try:
        a = int(input("Diga um número: "))
        b = int(input("Diga outro número: "))
        print(a/b)
        lista = [1,2]
        print(lista[3])
    except ValueError:
        print("Digita um número!!!")
    except ZeroDivisionError:
        print("Não dá para dividir por zero!!!")
    except Exception as e:
        print(f"algo deu errado!!! {e}")
    else:
        print("oi")



a = [5,8,1,7,9,4]
while True:
    try:
        print(a)
        i = int(input("Digite um índice da lista: "))
        print(a[i])
    except IndexError:
        print("Índice inexistente!!!")
    except ValueError:
        print("Apenas números podem ser digitados!!!")
    else:
        print("Parabéns, você sairá do loop")
        break


try:
    mensagem = "inteiro"
    a = int(input("Digite um número inteiro: "))
    mensagem = "flutuante"
    b = int(input("Digite um número float: "))
except ValueError:
        print(f"Digite um número {mensagem}!!")    



def acha_indice(lista, elem):
    for i in range(len(lista)):
        if lista[i]:
            return i
    raise ValueError(f"Não achei o {elem}")