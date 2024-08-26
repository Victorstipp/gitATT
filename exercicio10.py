def obter_ultimo_elemento(lista):
    if lista:
        return lista[-1]
    else:
        return None

lista = []
i = 1
while i <= 5:
    elem = int(input("Digite um elemento da lista: "))
    lista.append(elem)
    i += 1

    print("Lista atual:", lista)
    ultimo_elemento = obter_ultimo_elemento(lista)
    print("Último elemento da lista:", ultimo_elemento)
