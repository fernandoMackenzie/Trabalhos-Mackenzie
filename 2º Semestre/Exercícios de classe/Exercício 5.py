def intersec(a,b):
    lista = ""
    for x in range(len(a)):
        if a[x] not in b:
            lista = lista+" "+str(a[x])
    for x in range(len(b)):
        if b[x] not in a:
            lista = lista+" "+str(b[x])
    for x in range(len(a)):
        if a[x] in b:
            lista = lista+" "+str(a[x])
    return lista
            




a = [0]*3
b = [0]*3
for x in range(3):
    a[x] = int(input("Digite um número para o vetor A: "))
for x in range(3):
    b[x] = int(input("Digite um número para o vetor B: "))
result = intersec(a,b)
print("Intersecção = ",result)
