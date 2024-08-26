def mdc(a,b):
    if b ==0:
        return a
    else:
        return mdc(b,a%b)

#guarda os numeros digitados
num1= int(input("Digite um numero:"))
num2= int(input("Digite outro numero:"))

resultado=mdc(num1,num2)

print("MDC: ", resultado)
