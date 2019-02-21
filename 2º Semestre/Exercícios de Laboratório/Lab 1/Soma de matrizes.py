def gerar_mat(n,m):
    mat = []
    for i in range(n):
        linha = []
        for j in range(m):
            num = int(input("Digite um número para a matriz: "))
            linha.append(num)
        mat.append(linha)
    return mat

def soma_mat(a,b,n,m):
    c = []
    for i in range(n):
        linha = []
        for j in range(m):
            linha.append(a[i][j]+b[i][j])
        c.append(linha)
    return c

def print_mat(mat,n,m):
    for i in range(n):
        for j in range(m):
            print(mat[i][j], end=" ")
        print("\n")

n = int(input("Digite o número de linhas das matrizes: "))
m = int(input("Digite o número de colunas das matrizes: "))
print("Digite os números da matriz A: ")
a = gerar_mat(n,m)
print("Digite os números da matriz B: ")
b = gerar_mat(n,m)
c = soma_mat(a,b,n,m)
print("Soma A+B: ")
print_mat(c,n,m)
