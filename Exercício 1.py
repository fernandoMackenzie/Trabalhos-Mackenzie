def vetor(v):
    for i in range(len(v)-1):
        if v[i] > v[i+1]:
            return False
    return True

v = [0]*5
for x in range(5):
    v[x] = int(input("Digite um número inteiro: "))
resultado = vetor(v)
print(resultado)
