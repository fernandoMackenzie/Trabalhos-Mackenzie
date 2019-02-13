def entrada():
    num = int(input("Digite um número inteiro e positivo: "))
    while num <0:
        num = int(input("Número inválido...\n\nDigite um número positivo: "))
    return num

def calculaSoma(a,b,c):
    soma = a+b+c
    return soma

def main():
    a = entrada()
    b = entrada()
    c = entrada()
    soma = calculaSoma(a,b,c)
    print("A soma é: ",soma)

main()
    
    
