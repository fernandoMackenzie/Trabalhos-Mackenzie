def verifica(v):
    aux = 0
    diferentes = 0
    i = 0
    while aux <len(v):
        for x in range(len(v)-1):
            if v[aux] == v[x]:
                i += 1    
        if i == 1:
            diferentes +=1
        aux += 1
        i = 0
    return diferentes
                
            
        
        
    


v = [0]*10
for x in range(len(v)):
    v[x] = int(input("Digite um número inteiro: "))
resultado = verifica(v)
print("Números diferentes em V = ",resultado)
