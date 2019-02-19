def criar_mat(n,m):    
    mat =[]
    for i in range(n):
        linha=[]
        for j in range(m):
            num = int(input("Digite um número para a matriz: "))
            linha.append(num)
        mat.append(linha)
    return mat

    

n = int(input("Digite o número de linhas: "))
m = int(input("Digite o número de colunas: "))
mat = criar_mat(n,m)

print("Matriz principal: ")
for x in range(n):
    for y in range(m):
        print(mat[x][y], end =" ")
    print("\n")
    
print("Matriz transposta: ")
for x in range(n):
        for y in range(m):
            print(mat[y][x], end =" ")
        print("\n")
        





