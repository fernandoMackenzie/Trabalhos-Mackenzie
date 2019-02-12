def exp(n):
    i = 2
    h = 1
    a = 1
    for x in range(2,n+1):
        h += (a+x)/i
        a = a+x
        i += 2
    return h


n = int(input("Digite quantos termos da sequência serão calculados: "))
resultado = exp(n)
print("H = ",resultado)
