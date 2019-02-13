import random
def intersec(a,b):
    lista = []
    i = 0
    while i < len(a):
        for x in range(len(a)):
            if a[x] == b[i]:
                lista.append(a[x])  
        i += 1
    return lista
            




a = [0]*5
b = [0]*5
for x in range(5):
    a[x] = random.randint(0,10)
for x in range(5):
    b[x] = random.randint(0,10)
print("Vetor A = ",a)
print("Vetor B = ",b)
result = intersec(a,b)
print("Intersecção A com B = ",result)

