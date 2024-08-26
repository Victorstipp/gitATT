deslocamento = int(input("Digite o deslocamento: "))
texto = input("Digite o texto a ser criptografado: ")
texto_criptografado = ""

for letra in texto:#Este loop percorre cada caractere (letra) no texto.
    if letra.isupper():#Esse método verifica se todos os caracteres na string são letras maiúsculas se for verdadeira retorna true
        letra_criptografada = chr((ord(letra.lower()) + deslocamento - 97) % 26 + 65)
    elif letra.islower():#Esse método verifica se todos os caracteres na string são letras minusculas.
         letra_criptografada = chr((ord(letra) + deslocamento - 97) % 26 + 97)

    else: letra_criptografada = letra + texto_criptografado + letra_criptografada
    print("Texto criptografado:", texto_criptografado)