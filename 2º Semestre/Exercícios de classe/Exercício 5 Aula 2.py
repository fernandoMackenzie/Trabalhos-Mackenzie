import random
def uniao(a,b):
    lista = []
    i = 0
    for x in range(len(a)):
        lista.append(a[x])
    while i < len(a):
        flag = False
        for y in range(len(lista)):
            if lista[y] == b[i]:
                flag = True
        if flag == False:
            lista.append(b[i])
        i +=1
    return lista
            




a = [0]*5
b = [0]*5
for x in range(5):
    a[x] = random.randint(0,10)
for x in range(5):
    b[x] = random.randint(0,10)
print("Vetor A = ",a)
print("Vetor B = ",b)
result = uniao(a,b)
print("União de A com B = ",result)
