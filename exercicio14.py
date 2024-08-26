numeros = []
for i in range(10):
    try:
        numero = int(input("Digite um número inteiro: "))
        numeros.append(numero)
    except ValueError:
        print("Entrada inválida!!!")

# Verifica se a lista de números não está vazia para evitar divisão por zero
if numeros:
    soma = sum(numeros)
    media = soma / len(numeros)
    print("Soma:", soma)
    print("Média:", media)
else:
    print("Nenhum número válido foi inserido.")
