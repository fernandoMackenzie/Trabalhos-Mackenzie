import random
def dif(a,b):
    lista = []
    i = 0
    while i < len(a):
        flag = False
        for x in range(len(a)):
            if b[x] == a[i]:
                flag = True
        if flag == False:
            lista.append(a[i])
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
result = dif(a,b)
print("Diferença A - B = ",result)
