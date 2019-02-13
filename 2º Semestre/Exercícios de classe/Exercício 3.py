def intersec(a,b):
    lista = ""
    for x in range(len(a)):
        if a[x]in b:
            lista = lista+" "+str(a[x])
    return lista
            




a = [0]*5
b = [0]*5
for x in range(5):
    a[x] = int(input("Digite um número para o vetor A: "))
for x in range(5):
    b[x] = int(input("Digite um número para o vetor B: "))
result = intersec(a,b)
print("Intersecção = ",result)
