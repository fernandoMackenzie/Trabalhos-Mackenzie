def mult(a,b):
    res = 0
    for x in range(b):
        res += a
    return res

def pot(a,b):
    res = 0
    for x in range(b):
        res += mult(a,a)
    return res

a = int(input("Digite A: "))
b = int(input("Digite B: "))
res = pot(a,b)
print("Resultado = ",res)
