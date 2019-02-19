def posicao(v,x):
    aux = -2 
    for i in range(len(v)):
        if v[i] == x:
            aux = i
    if aux == -2:
        return -1
    else:
        return aux






v = [0]*5
for x in range(len(v)):
    v[x] = int(input("Digite um número: "))
x = int(input("Digite o numero do qual deseja saber sua posição no vetor: "))
print("A posição de ",x," no vetor é V: ",posicao(v,x))
