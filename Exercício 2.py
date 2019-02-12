def inverter(v):
    for i in range(len(v)//2):
        aux = v[i]
        v[i] = v[len(v)-1-i]
        v[len(v)-1-i] = aux
    return v



v = [0]*5
for x in range(5):
    v[x] = int(input("Digite um número inteiro: "))
resultado = inverter(v)
print("Vetor invertido = ",resultado)
