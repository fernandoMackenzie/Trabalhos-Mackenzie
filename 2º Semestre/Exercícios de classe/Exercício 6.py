#4) Escreva uma função que preencha por leitura do teclado um vetor de 10 posições e retorna a quantidade de valores diferentes existem no vetor.

def diferentes(v):
    aux = 0
    i = 0
    while i <len(v):
        flag = True
        for x in range(i+1,len(v)):
            if v[i] == v[x]:
                flag = False
        if flag == True:
            aux +=1
        i += 1
    return aux
        
            






v = [0]*10
for x in range(len(v)):
    v[x] = int(input("Digite um numero inteiro: "))
resultado = diferentes(v)
print("Diferentes em v: ", resultado)
